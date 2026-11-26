"""부족 단원 보강용 수학 생성기 (연립방정식·무리함수·명제·함수·유리함수·복소수·삼차방정식·집합)"""
import math, itertools, random
from fractions import Fraction as F
from common import fr, rad, num_opts, uniq
import gen_math as G

rng = random.Random(4242)
OUT = []
def add(unit, lvl, src, q, opts, ans, exp):
    import re as _re
    fx = lambda t: _re.sub(r'(?<![\d.])1i', 'i', G._clean(t))
    q, exp, opts, ans = fx(q), fx(exp), [fx(o) for o in opts], fx(ans)
    assert ans in opts and uniq(opts) and len(opts) == 5, (q, opts, ans)
    OUT.append(dict(unit=unit, lvl=lvl, src=src, q=q, opts=opts, ans=ans, exp=exp))
def times(t, n, maxtry=8000):
    seen = set(); got = 0; k = 0
    while got < n and k < maxtry:
        k += 1; r = t()
        if r is None or r[3] in seen: continue
        seen.add(r[3]); add(*r); got += 1
P = G.poly_str; L = G.lin

# ---------- 연립방정식 ----------
def s1():  # x+y, xy → 대칭식
    x, y = rng.sample(range(-6, 8), 2)
    s, p = x + y, x * y
    if p == 0: return None
    kind = rng.choice(["sq", "cube", "diff2", "inv"])
    if kind == "sq": v = F(s * s - 2 * p); w = "x²+y²"; e = f"(x+y)²−2xy={s*s}−({2*p})={fr(v)}"
    elif kind == "cube": v = F(s ** 3 - 3 * p * s); w = "x³+y³"; e = f"(x+y)³−3xy(x+y)={fr(v)}"
    elif kind == "diff2": v = F(s * s - 4 * p); w = "(x−y)²"; e = f"(x+y)²−4xy={fr(v)}"
    else:
        if p == 0: return None
        v = F(s, p); w = "1/x+1/y"; e = f"(x+y)/xy={s}/{p}={fr(v)}"
    o, a = num_opts(v, rng)
    return ("연립방정식", 2, "교과서 심화", f"x+y={s}, xy={p}일 때, {w}의 값은?", o, a, e + ".")
times(s1, 18)

def s2():  # 연립이차방정식 해 → 곱/합
    a, b = rng.randint(1, 6), rng.randint(-5, 5)
    # x−y=b 이고 x²+y²=c (해가 정수가 되도록 x,y 먼저)
    x = rng.randint(-6, 7); y = x - b
    c = x * x + y * y
    # 두 해 (x,y)와 (−y,−x)  → x−y=b 유지
    sols = {(x, y), (-y, -x)}
    kind = rng.choice(["maxsum", "prod"])
    if kind == "maxsum":
        v = max(p + q for p, q in sols); qq = "x+y의 최댓값"; e = f"y=x−({b})를 대입하면 해 " + ", ".join(f"({p},{q})" for p, q in sorted(sols)) + f" → x+y의 최댓값 {v}"
    else:
        vals = {p * q for p, q in sols}
        if len(vals) != 1: return None
        v = vals.pop(); qq = "xy의 값"; e = f"(x−y)²=x²+y²−2xy → {b*b}={c}−2xy → xy={v}"
    o, ans = num_opts(v, rng)
    return ("연립방정식", 3, "모의고사형", f"연립방정식 x−y={b}, {G.eul('x²+y²='+str(c))} 만족시키는 실수 x, y에 대하여 {qq}은?".replace("의 값은", "의 값은"), o, ans, e + ".")
times(s2, 16)

def s3():  # 공통근 / 해의 조건
    r = rng.randint(-4, 5); a = rng.randint(-5, 5); b = rng.randint(-5, 5)
    # x²+ax+k=0, x²+bx+m=0 가 공통근 r 을 가짐 → k=-(r²+ar), m=-(r²+br)
    if a == b: return None
    k = -(r * r + a * r); m = -(r * r + b * r)
    kind = rng.choice(["r", "km"])
    if kind == "r":
        o, ans = num_opts(r, rng)
        return ("연립방정식", 3, "EBS형", f"두 이차방정식 {P([1,a,k])}=0, {P([1,b,m])}=0의 공통근은?", o, ans,
                f"두 식을 빼면 ({a}−({b}))x+({k}−({m}))=0 → x={r}.")
    v = k + m
    o, ans = num_opts(v, rng)
    return ("연립방정식", 3, "모의고사형", f"두 이차방정식 {P([1,a,0])}+k=0, {P([1,b,0])}+m=0이 공통근 {G.eul(str(r))} 가질 때, k+m의 값은?", o, ans,
            f"x={r} 대입: k={k}, m={m} → {v}.")
times(s3, 16)

# ---------- 무리함수 ----------
def r1():  # y=√(a(x−p))+q 정의역/치역 결합
    a = rng.choice([1, 2, 3, -1, -2]); p = rng.randint(-4, 5); q = rng.randint(-4, 5)
    kind = rng.choice(["dom", "rng", "val"])
    inner = f"{a if a not in (1,-1) else ('' if a==1 else '−')}(x{'−' if p>=0 else '+'}{abs(p)})".replace("(x−0)", "x").replace("(x+0)", "x")
    fstr = f"y=√({inner}){'+' if q>=0 else '−'}{abs(q)}".replace("+0", "").replace("−0", "")
    if kind == "dom":
        ans = f"x≥{p}" if a > 0 else f"x≤{p}"
        o = [f"x≥{p}", f"x≤{p}", f"x≥{-p}", f"x≤{-p}", f"x≥{q}"] if p != 0 and p != -p else None
        if not o or len(set(o)) < 5: return None
        rng.shuffle(o)
        return ("무리함수", 2, "교과서 심화", f"함수 {fstr}의 정의역은?", o, ans, f"근호 안이 0 이상: {a}(x−{p})≥0 → {ans}.")
    if kind == "rng":
        ans = f"y≥{q}"; o = [f"y≥{q}", f"y≤{q}", f"y≥{p}", f"y≤{p}", f"y≥{q+1}"]
        if len(set(o)) < 5: return None
        rng.shuffle(o)
        return ("무리함수", 2, "교과서 심화", f"함수 {fstr}의 치역은?", o, ans, f"√ 값은 0 이상 → y≥{q}.")
    t = rng.randint(1, 4); x0 = p + F(t * t, a)
    if x0.denominator != 1: return None
    v = t + q
    o, an = num_opts(v, rng)
    return ("무리함수", 2, "교과서 심화", f"함수 {fstr}에서 x={fr(x0)}일 때 함숫값은?", o, an, f"√({a}·({fr(x0)}−{p}))=√{t*t}={t} → {v}.")
times(r1, 24)

def r2():  # 구간 최대최소
    a = rng.choice([1, 2, 3]); p = rng.randint(-3, 3); q = rng.randint(-3, 4)
    ts = [t for t in range(0, 7)]
    lo, hi = sorted(rng.sample(ts, 2))
    x1, x2 = p + F(lo * lo, a), p + F(hi * hi, a)
    if x1.denominator != 1 or x2.denominator != 1: return None
    sign = rng.choice([1, -1])
    if sign == 1: M, m = hi + q, lo + q; fs = f"√({a if a>1 else ''}(x{'−' if p>=0 else '+'}{abs(p)}))+{q}"
    else: M, m = -lo + q, -hi + q; fs = f"−√({a if a>1 else ''}(x{'−' if p>=0 else '+'}{abs(p)}))+{q}"
    fs = fs.replace("(x−0)", "x").replace("+−", "−").replace("+0", "")
    o, ans = num_opts(M + m, rng)
    return ("무리함수", 3, "모의고사형", f"{fr(x1)}≤x≤{fr(x2)}에서 함수 y={fs}의 최댓값을 M, 최솟값을 m이라 할 때, M+m의 값은?", o, ans,
            f"{'증가' if sign==1 else '감소'}함수이므로 양 끝값에서 최대·최소: M={M}, m={m} → {M+m}.")
times(r2, 20)

def r3():  # 역함수
    a = rng.choice([1, 2, 3, 4]); p = rng.randint(-3, 4); q = rng.randint(-3, 4); t = rng.randint(1, 5)
    # f(x)=√(a(x−p))+q, f⁻¹(t+q) = p + t²/a
    x = p + F(t * t, a)
    o, ans = num_opts(x, rng)
    fs = f"√({a if a>1 else ''}(x{'−' if p>=0 else '+'}{abs(p)})){'+' if q>=0 else '−'}{abs(q)}".replace("(x−0)", "x").replace("+0", "").replace("−0", "")
    return ("무리함수", 3, "EBS형", f"함수 f(x)={fs}의 역함수를 g(x)라 할 때, g({t+q})의 값은?", o, ans,
            f"f(x)={t+q} ⇔ √({a}(x−{p}))={t} ⇔ x={p}+{t*t}/{a}={ans}.")
times(r3, 16)

# ---------- 명제 ----------
def m1():  # 필요조건
    p, q = sorted(rng.sample(range(-6, 10), 2)); r = rng.randint(1, 3)
    if q - p < 2: return None
    # p: x²−(p+q)x+pq≤0 이 |x−a|≤r 이기 위한 충분조건 → [p,q]⊆[a−r,a+r]
    if q - p > 2 * r:
        r = (q - p + 1) // 2 + rng.randint(0, 2)
    cnt = 2 * r - (q - p) + 1
    if cnt <= 0: return None
    o, ans = num_opts(cnt, rng, lo=1)
    return ("명제", 3, "모의고사형", f"두 조건 p: {P([1,-(p+q),p*q])}≤0, q: |x−a|≤{r}에 대하여 p가 q이기 위한 충분조건이 되도록 하는 정수 a의 개수는?", o, ans,
            f"[{p},{q}]⊆[a−{r}, a+{r}] → {q-r}≤a≤{p+r} → {cnt}개.")
times(m1, 16)

def m2():  # 명제의 참·거짓 (참인 명제 개수) — 정수 범위 명제
    N = rng.randint(10, 30)
    a, b = rng.choice([(2, 4), (3, 6), (2, 6), (4, 2), (6, 3), (6, 2), (3, 9), (9, 3)])
    true = (b % a == 0)  # "b의 배수이면 a의 배수이다"는 a|b일 때 참
    cand = [(f"자연수 n이 {b}의 배수이면 n은 {a}의 배수이다.", b % a == 0),
            (f"자연수 n이 {a}의 배수이면 n은 {b}의 배수이다.", a % b == 0),
            ("실수 x에 대하여 x²=1이면 x=1이다.", False),
            ("실수 x에 대하여 x>1이면 x²>1이다.", True),
            ("두 실수 a, b에 대하여 ab=0이면 a=0이다.", False),
            ("두 실수 a, b에 대하여 a²+b²=0이면 a=b=0이다.", True),
            ("실수 x에 대하여 |x|<1이면 x²<1이다.", True),
            ("두 자연수 m, n에 대하여 m+n이 짝수이면 m, n은 모두 짝수이다.", False),
            ("두 실수 a, b에 대하여 a>b이면 a²>b²이다.", False),
            ("두 정수 m, n에 대하여 mn이 홀수이면 m, n은 모두 홀수이다.", True)]
    pick = rng.sample(cand, 3)
    if len({c[0] for c in pick}) < 3: return None
    lab = "ㄱㄴㄷ"
    ans = ", ".join(lab[i] for i, c in enumerate(pick) if c[1])
    if not ans: return None
    COMB = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄱ, ㄴ', 'ㄱ, ㄷ', 'ㄴ, ㄷ', 'ㄱ, ㄴ, ㄷ']
    i = COMB.index(ans); stt = rng.choice([s for s in range(3) if s <= i < s + 5])
    o = COMB[stt:stt + 5]
    q = "다음 명제 중 참인 것만을 <보기>에서 있는 대로 고른 것은?\n" + "\n".join(f"{lab[i]}. {c[0]}" for i, c in enumerate(pick))
    e = " ".join(f"{lab[i]}({'참' if c[1] else '거짓'})" for i, c in enumerate(pick)) + ". 거짓인 명제는 반례 하나로 확인한다(예: x=−1, a<0인 경우 등)."
    return ("명제", 3, "모의고사형", q, o, ans, e)
times(m2, 18)

# ---------- 함수 ----------
def f1():  # 일대일대응 / 함수 개수
    n, m = rng.randint(2, 4), rng.randint(2, 5)
    kind = rng.choice(["all", "inj", "bij", "inc"])
    if kind == "all": v = m ** n; d = "함수"; e = f"각 원소마다 {m}가지 → {m}^{n}={v}"
    elif kind == "inj":
        if m < n: return None
        v = math.perm(m, n); d = "일대일함수"; e = f"ₘPₙ={v}"
    elif kind == "bij":
        if m != n: return None
        v = math.factorial(n); d = "일대일대응"; e = f"{n}!={v}"
    else:
        if m <= n: return None
        v = math.comb(m, n); d = "x₁<x₂이면 f(x₁)<f(x₂)를 만족시키는 함수"; e = f"공역에서 {n}개를 고르면 순서가 정해짐: ₘCₙ={v}"
    X = "{" + ",".join(map(str, range(1, n + 1))) + "}"; Y = "{" + ",".join("abcde"[:m]) + "}" if kind != "inc" else "{" + ",".join(map(str, range(1, m + 1))) + "}"
    o, ans = num_opts(v, rng, lo=1)
    return ("함수", 2, "교과서 심화", f"집합 X={X}에서 Y={Y}로의 {d}의 개수는?", o, ans, e + ".")
times(f1, 14)

def f2():  # 합성함수 값
    a, b, c, d = rng.randint(1, 4), rng.randint(-5, 5), rng.randint(-3, 3), rng.randint(-4, 5)
    x0 = rng.randint(-3, 4)
    f = lambda x: a * x + b; g = lambda x: x * x + c * x + d
    kind = rng.choice(["fg", "gf", "ff"])
    if kind == "fg": v = f(g(x0)); w = f"(f∘g)({x0})"
    elif kind == "gf": v = g(f(x0)); w = f"(g∘f)({x0})"
    else: v = f(f(x0)); w = f"(f∘f)({x0})"
    o, ans = num_opts(v, rng)
    return ("함수", 2, "교과서 심화", f"두 함수 f(x)={L(a,b)}, g(x)={P([1,c,d])}에 대하여 {w}의 값은?", o, ans, f"안쪽 함수부터 계산하면 {v}.")
times(f2, 14)

# ---------- 유리함수 ----------
def q1():  # 점근선 교점 + 평행이동
    p, q, k = rng.randint(-4, 4), rng.randint(-4, 4), rng.choice([1, 2, 3, -1, -2, 4])
    m, n = rng.randint(-3, 3), rng.randint(-3, 3)
    # y=k/x 를 x축 p, y축 q 평행이동 → y = k/(x−p)+q = (qx −pq + k)/(x−p)
    kind = rng.choice(["asym", "shift"])
    num = P([q, -p * q + k]); den = L(1, -p)
    if kind == "asym":
        v = p + q
        o, ans = num_opts(v, rng)
        return ("유리함수", 2, "교과서 심화", f"함수 y=({num})/({den})의 그래프의 두 점근선의 교점을 (a, b)라 할 때, a+b의 값은?", o, ans,
                f"y={q}+({k})/(x−({p})) → 점근선 x={p}, y={q} → {v}.")
    v = (p + m) * (q + n)
    o, ans = num_opts(v, rng)
    return ("유리함수", 3, "모의고사형", f"함수 y=({num})/({den})의 그래프를 x축 방향으로 {m}만큼, y축 방향으로 {n}만큼 평행이동한 그래프의 점근선이 x=a, y=b일 때, ab의 값은?", o, ans,
            f"원래 점근선 x={p}, y={q} → 이동 후 x={p+m}, y={q+n} → ab={v}.")
times(q1, 18)

# ---------- 복소수 ----------
def c1():
    a, b, c, d = [rng.randint(-5, 5) for _ in range(4)]
    if b == 0 or d == 0: return None
    z = complex(a, b) * complex(c, d)
    kind = rng.choice(["re", "im", "conj"])
    if kind == "re": v = int(z.real); w = "실수부분"
    elif kind == "im": v = int(z.imag); w = "허수부분"
    else:
        zz = complex(a, b) * complex(a, -b); v = int(zz.real); w = None
    if w:
        o, ans = num_opts(v, rng)
        return ("복소수", 2, "교과서 심화", f"({a}{'+' if b>0 else '−'}{abs(b)}i)({c}{'+' if d>0 else '−'}{abs(d)}i)의 {w}은?", o, ans, f"전개하면 {int(z.real)}{'+' if z.imag>=0 else '−'}{abs(int(z.imag))}i → {v}.")
    o, ans = num_opts(v, rng)
    return ("복소수", 2, "교과서 심화", f"z={a}{'+' if b>0 else '−'}{abs(b)}i일 때, z·z̄의 값은? (z̄는 z의 켤레복소수)", o, ans, f"z·z̄=a²+b²={v}.")
times(c1, 12)

def c2():
    n = rng.randint(10, 200)
    s = sum(1j ** k for k in range(1, n + 1))
    re, im = round(s.real), round(s.imag)
    ans = (f"{re}" if re else "") + (("+" if im > 0 and re else "") + ("" if abs(im) != 1 else ("−" if im < 0 else "")) + (str(abs(im)) if abs(im) != 1 else "") + "i" if im else "")
    ans = ans or "0"
    if im < 0 and abs(im) != 1: ans = ans.replace(str(abs(im)) + "i", "−" + str(abs(im)) + "i") if not re else ans.replace("+", "")
    o = ["0", "i", "−1", "−1+i", "−1−i", "1", "−i", "1+i"]
    norm = {complex(0, 0): "0", 1j: "i", -1: "−1", complex(-1, 1): "−1+i", complex(-1, -1): "−1−i", 1: "1", -1j: "−i", complex(1, 1): "1+i"}
    key = complex(re, im)
    if key not in norm: return None
    ans = norm[key]
    opts = [ans] + rng.sample([x for x in o if x != ans], 4); rng.shuffle(opts)
    return ("복소수", 3, "모의고사형", f"i+i²+i³+…+i^{n}의 값은?", opts, ans, f"네 항마다 합이 0. {n}={n//4}×4+{n%4} → 처음 {n%4}개 항의 합 = {ans}.")
times(c2, 10)

# ---------- 삼차방정식 ----------
def k1():  # 인수정리로 나머지 두 근
    r = rng.randint(-3, 3); a, b = rng.randint(-4, 4), rng.randint(-5, 5)
    # (x−r)(x²+ax+b) 전개
    cs = [1, a - r, b - a * r, -b * r]
    kind = rng.choice(["sum", "prod"])
    v = -a if kind == "sum" else b
    o, ans = num_opts(v, rng)
    return ("삼차방정식", 3, "EBS형", f"삼차방정식 {P(cs)}=0의 한 근이 {r}일 때, 나머지 두 근의 {'합' if kind=='sum' else '곱'}은?", o, ans,
            f"조립제법으로 (x−{r})({P([1,a,b])})=0 → 나머지 두 근의 {'합 '+str(-a) if kind=='sum' else '곱 '+str(b)}.")
times(k1, 12)

# ---------- 집합 ----------
def e1():
    U = rng.randint(30, 60); a = rng.randint(10, 25); b = rng.randint(8, 22); ab = rng.randint(2, min(a, b) - 1)
    if a + b - ab > U: return None
    kind = rng.choice(["union", "comp", "only"])
    if kind == "union": v = a + b - ab; w = "n(A∪B)"; e = f"{a}+{b}−{ab}={v}"
    elif kind == "comp": v = U - (a + b - ab); w = "n(Aᶜ∩Bᶜ)"; e = f"n((A∪B)ᶜ)={U}−{a+b-ab}={v}"
    else: v = a - ab; w = "n(A−B)"; e = f"{a}−{ab}={v}"
    o, ans = num_opts(v, rng, lo=0)
    return ("집합", 2, "교과서 심화", f"전체집합 U의 두 부분집합 A, B에 대하여 n(U)={U}, n(A)={a}, n(B)={b}, n(A∩B)={ab}일 때, {w}의 값은?", o, ans, e + ".")
times(e1, 10)

if __name__ == "__main__":
    from collections import Counter
    print(len(OUT), Counter(o["unit"] for o in OUT))
    for o in OUT[::14]: print(o["q"], o["opts"], o["ans"], "|", o["exp"])
