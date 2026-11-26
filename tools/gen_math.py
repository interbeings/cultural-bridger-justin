import math, itertools, cmath
from fractions import Fraction as F
import random
import numpy as np
from common import fr, rad, num_opts, uniq

rng = random.Random(77)
MULT = 4
OUT = []
def _clean(t):
    t = t.replace("+-", "−").replace("−-", "+").replace("--", "+").replace("-", "−")
    t = t.replace("(+", "(").replace("=+", "=")
    return t
def add(unit, lvl, src, q, opts, ans, exp):
    q, exp = _clean(q), _clean(exp)
    assert ans in opts and uniq(opts) and len(opts) == 5, (q, opts, ans)
    OUT.append(dict(unit=unit, lvl=lvl, src=src, q=q, opts=opts, ans=ans, exp=exp))

def poly_str(cs, var="x"):
    """계수 리스트(최고차부터) -> 문자열"""
    n = len(cs) - 1; out = ""
    sup = {2: "²", 3: "³", 4: "⁴", 5: "⁵"}
    for i, c in enumerate(cs):
        d = n - i
        if c == 0: continue
        sign = "−" if c < 0 else "+"
        a = abs(c)
        coef = "" if (a == 1 and d > 0) else fr(a)
        term = coef + (var + sup.get(d, "") if d > 1 else (var if d == 1 else ""))
        if out == "": out = ("−" if c < 0 else "") + term
        else: out += f"{sign}{term}"
    return out


def _last_digit(t):
    for ch in reversed(t):
        if ch.isdigit(): return ch
        if ch in ")": continue
        if ch.isalpha(): return ch
    return "1"
def ro(t):
    d=_last_digit(t)
    return t+("으로" if d in "036" else "로")
def eul(t):
    d=_last_digit(t)
    return t+("을" if d in "013678" else "를")
def gwa(t):
    d=_last_digit(t)
    return t+("과" if d in "013678" else "와")

def lin(a, b):  # ax+b
    return poly_str([a, b])

def times(templ, n, maxtry=400):
    got = 0; seen = set(); t = 0
    while got < n and t < maxtry:
        t += 1
        r = templ()
        if r is None: continue
        key = r[3]
        if key in seen: continue
        seen.add(key); add(*r); got += 1

# 1 나머지정리
def t1():
    p, q = sorted(rng.sample(range(-3, 4), 2))
    r = rng.choice([x for x in range(-4, 5) if x not in (p, q)])
    a, b = rng.randint(-4, 5), rng.randint(-6, 7)
    tval = rng.randint(-3, 4)
    if tval == 0 or a == 0: return None
    c = tval * (r - p) * (r - q) + a * r + b
    s = rng.choice([x for x in range(-4, 6) if x not in (p, q, r)])
    R = tval * (s - p) * (s - q) + a * s + b
    div = poly_str([1, -(p + q), p * q])
    o, ans = num_opts(R, rng)
    return ("다항식", 3, "모의고사형",
            f"다항식 P(x)를 {ro(div)} 나눈 나머지는 {lin(a,b)}이고, {ro(lin(1,-r))} 나눈 나머지는 {fr(c)}이다. P(x)를 {ro('('+div+')('+lin(1,-r)+')')} 나눈 나머지를 R(x)라 할 때, R({fr(s)})의 값은?".replace("x+0", "x").replace("x−0", "x"),
            o, ans,
            f"R(x)=k(x−{p})(x−{q})+{lin(a,b)} 꼴. R({r})=P({r})={c}에서 k={tval}. R({s})={R}.".replace("−-", "+"))
times(t1, 8*MULT, maxtry=3000)

# 2 x+1/x=k → x^n+1/x^n
def t2():
    k = rng.randint(3, 7); n = rng.choice([3, 4, 5])
    s = [2, k]
    for i in range(2, n + 1): s.append(k * s[-1] - s[-2])
    o, ans = num_opts(s[n], rng)
    sup = {3: "³", 4: "⁴", 5: "⁵"}[n]
    return ("다항식", 3 if n < 5 else 4, "EBS형",
            f"x+1/x={k}일 때, x{sup}+1/x{sup}의 값은?", o, ans,
            f"aₙ=xⁿ+1/xⁿ라 하면 aₙ={k}aₙ₋₁−aₙ₋₂ (a₀=2, a₁={k}). " + ", ".join(f"a{i}={s[i]}" for i in range(2, n + 1)) + ".")
times(t2, 10*MULT, maxtry=3000)

# 3 a+b+c, ab+bc+ca, abc → a³+b³+c³ 또는 a²+b²+c²
def t3():
    s, p, r = rng.randint(-3, 5), rng.randint(-6, 6), rng.randint(-5, 6)
    kind = rng.choice([3, 2])
    if kind == 3:
        v = s ** 3 - 3 * s * p + 3 * r
        o, ans = num_opts(v, rng)
        return ("다항식", 3, "모의고사형",
                f"a+b+c={fr(s)}, ab+bc+ca={fr(p)}, abc={fr(r)}일 때, a³+b³+c³의 값은?", o, ans,
                f"a³+b³+c³=(a+b+c)³−3(a+b+c)(ab+bc+ca)+3abc={s**3}−({3*s*p})+{3*r}={v}.")
    else:
        m = rng.randint(1, 6)
        v = 2 * m * m
        o, ans = num_opts(v, rng)
        return ("다항식", 3, "수능형",
                f"실수 a, b, c가 a+b+c=0, a²+b²+c²={2*m}을 만족시킬 때, a⁴+b⁴+c⁴의 값은?", o, ans,
                f"ab+bc+ca=−{m}. a²b²+b²c²+c²a²=(ab+bc+ca)²−2abc(a+b+c)={m*m}. 답 {(2*m)**2}−2·{m*m}={v}.")
times(t3, 10*MULT, maxtry=3000)

# 4 삼차방정식 근과 계수
def t4():
    b, c, d = rng.randint(-4, 4), rng.randint(-5, 5), rng.randint(-6, 6)
    if d == 0: return None
    f = lambda x: x ** 3 + b * x ** 2 + c * x + d
    s = -b
    kind = rng.choice(["pair", "plus1", "minus2"])
    eq = poly_str([1, b, c, d]) + "=0"
    if kind == "pair":
        v = f(s); qq = "(α+β)(β+γ)(γ+α)"; e = f"α+β+γ={s} → α+β={s}−γ 등. 곱은 f({s})={v} (f(x)={poly_str([1,b,c,d])})."
    elif kind == "plus1":
        v = -f(-1); qq = "(1+α)(1+β)(1+γ)"; e = f"f(x)=(x−α)(x−β)(x−γ)이므로 f(−1)=−(1+α)(1+β)(1+γ). 답 −f(−1)={v}."
    else:
        v = f(2); qq = "(2−α)(2−β)(2−γ)"; e = f"f(2)=(2−α)(2−β)(2−γ)={v}."
    o, ans = num_opts(v, rng)
    return ("삼차방정식", 3, "모의고사형", f"삼차방정식 {eq}의 세 근을 α, β, γ라 할 때, {qq}의 값은?", o, ans, e)
times(t4, 10*MULT, maxtry=3000)

# 5 이차방정식 근 대칭식
def t5():
    p, q = rng.randint(-6, 7), rng.randint(-5, 6)
    if q == 0 or p == 0: return None
    kind = rng.choice(["sq", "cube", "inv2", "diff"])
    eq = poly_str([1, -p, q]) + "=0"
    if kind == "sq": v = F(p * p - 2 * q); qq = "α²+β²"; e = f"α+β={p}, αβ={q} → (α+β)²−2αβ={fr(v)}."
    elif kind == "cube": v = F(p ** 3 - 3 * p * q); qq = "α³+β³"; e = f"(α+β)³−3αβ(α+β)={p**3}−({3*p*q})={fr(v)}."
    elif kind == "inv2": v = F(p * p - 2 * q, q * q); qq = "1/α²+1/β²"; e = f"(α²+β²)/(αβ)²=({p*p-2*q})/{q*q}={fr(v)}."
    else: v = F(p * p - 4 * q); qq = "(α−β)²"; e = f"(α+β)²−4αβ={fr(v)}."
    o, ans = num_opts(v, rng)
    return ("이차방정식", 2, "교과서 심화", f"이차방정식 {eq}의 두 근을 α, β라 할 때, {qq}의 값은?", o, ans, e)
times(t5, 10*MULT, maxtry=3000)

# 6 포물선과 직선이 접할 때
def t6():
    m, n = rng.randint(-4, 5), rng.randint(-5, 6)
    # y=x²−2kx+k²+k+c 와 y=mx+n 접할 때 k
    k0 = rng.randint(-6, 6)
    # x²−(2k+m)x+k²+k+c−n=0, D/4=(2k+m)²/4−(k²+k+c−n) = km + m²/4 − k − c + n = 0
    # 선형 in k: k(m−1) = c − n − m²/4. choose m odd/even to make integer: m even
    if m % 2 or m == 1 or m == 0: return None
    c = k0 * (m - 1) + n + m * m // 4
    o, ans = num_opts(k0, rng)
    return ("이차함수", 3, "모의고사형",
            f"이차함수 y=x²−2kx+k²+k{'+' if c>=0 else '−'}{abs(c)}의 그래프가 직선 y={lin(m,n)}에 접할 때, 상수 k의 값은?".replace("+0의", "의").replace("y=0", "y=0"),
            o, ans, f"x²−(2k+{m})x+k²+k+{c}−({n})=0의 판별식 D/4=0 → k({m}−1)={c}−({n})−{m*m//4} → k={k0}.".replace("+-", "−"))
times(t6, 8*MULT, maxtry=3000)

# 7 구간 최대최소 합
def t7():
    h = rng.randint(-3, 4); c = rng.randint(-5, 6); p, q = sorted(rng.sample(range(-3, 6), 2))
    if q - p < 2: return None
    f = lambda x: x * x - 2 * h * x + c
    xs = [p, q] + ([h] if p <= h <= q else [])
    M, m = max(f(x) for x in xs), min(f(x) for x in xs)
    o, ans = num_opts(M + m, rng)
    return ("이차함수", 2, "교과서 심화",
            f"{p}≤x≤{q}에서 이차함수 f(x)={poly_str([1,-2*h,c])}의 최댓값을 M, 최솟값을 m이라 할 때, M+m의 값은?",
            o, ans, f"꼭짓점 x={h}. 구간 양 끝과 꼭짓점(구간 안일 때)의 값을 비교: M={M}, m={m} → {M+m}.")
times(t7, 8*MULT, maxtry=3000)

# 8 절댓값 부등식 정수해
def t8():
    a, b = sorted(rng.sample(range(-6, 7), 2)); c = rng.randint(b - a + 1, b - a + 10)
    cnt = len([x for x in range(-60, 60) if abs(x - a) + abs(x - b) <= c])
    o, ans = num_opts(cnt, rng)
    s1 = f"x{'−' if a>=0 else '+'}{abs(a)}"; s2 = f"x{'−' if b>=0 else '+'}{abs(b)}"
    lo = F(a + b - c, 2); hi = F(a + b + c, 2)
    return ("부등식", 2, "교과서 심화", f"부등식 {eul("|"+s1+"|+|"+s2+"|≤"+str(c))} 만족시키는 정수 x의 개수는?".replace("x−0", "x").replace("x+0", "x"),
            o, ans, f"해는 {fr(lo)}≤x≤{fr(hi)} → 정수 {cnt}개.")
times(t8, 8*MULT, maxtry=3000)

# 9 항상 성립
def t9():
    a = rng.randint(-3, 4); c = rng.randint(2, 9)
    o, ans = num_opts(c, rng, lo=1)
    ka = f"k{'−' if a>=0 else '+'}{abs(a)}".replace("k−0", "k")
    return ("부등식", 3, "모의고사형",
            f"모든 실수 x에 대하여 ({ka})x²−2({ka})x+{c}>0이 성립하도록 하는 정수 k의 개수는?", o, ans,
            f"k={a}이면 {c}>0 성립. k>{a}이면 D/4=({ka})²−{c}({ka})<0 → {a}<k<{a+c}. 합쳐서 {a}≤k≤{a+c-1} → {c}개.")
times(t9, 8*MULT, maxtry=3000)

# 10 근의 분리
def t10():
    m = rng.randint(4, 12); t = rng.choice([1, 2])
    # x²−2ax+a+m=0 두 근 모두 t보다 큼
    cnt = [a for a in range(-50, 50) if a * a - a - m >= 0 and a > t and t * t - 2 * a * t + a + m > 0]
    if not cnt: return None
    o, ans = num_opts(len(cnt), rng, lo=1)
    return ("이차방정식", 3, "수능형",
            f"이차방정식 x²−2ax+a+{m}=0의 두 근이 모두 {t}보다 크도록 하는 정수 a의 개수는?", o, ans,
            f"D/4=a²−a−{m}≥0, 축 a>{t}, f({t})={t*t}−{2*t}a+a+{m}>0 을 모두 만족 → a={', '.join(map(str,cnt))} ({len(cnt)}개).")
times(t10, 7*MULT, maxtry=3000)

# 11 숫자 카드 배수
def t11():
    n = rng.choice([5, 6, 7]); k = rng.choice([3, 4, 5]); d = rng.choice([3, 3, 2, 5])
    digs = list(range(1, n + 1))
    if d == 4 or k == 4 and d == 2: pass
    cnt = sum(1 for p in itertools.permutations(digs, 3) if int("".join(map(str, p))) % d == 0) if k == 3 else None
    if k != 3: return None
    o, ans = num_opts(cnt, rng)
    return ("경우의 수", 2, "모의고사형",
            f"1부터 {n}까지의 자연수 중 서로 다른 세 수를 택해 만들 수 있는 세 자리 자연수 중 {d}의 배수의 개수는?", o, ans,
            f"{d}의 배수 조건({'각 자리 합이 3의 배수' if d==3 else '일의 자리 조건'})으로 세면 {cnt}개.")
times(t11, 6*MULT, maxtry=3000)

# 12 빈 상자 없는 분배
def t12():
    n = rng.randint(4, 7); b = rng.choice([2, 3])
    v = sum((-1) ** i * math.comb(b, i) * (b - i) ** n for i in range(b + 1))
    o, ans = num_opts(v, rng)
    return ("경우의 수", 3, "수능형", f"서로 다른 공 {n}개를 서로 다른 상자 {b}개에 빈 상자가 없도록 넣는 경우의 수는?", o, ans,
            f"포함배제: " + ("3ⁿ−3·2ⁿ+3" if b == 3 else "2ⁿ−2") + f" (n={n}) = {v}.")
times(t12, 7*MULT, maxtry=3000)

# 13 정다각형 삼각형
def t13():
    n = rng.randint(7, 14); kind = rng.choice(["none", "one"])
    if kind == "none": v = n * (n - 4) * (n - 5) // 6; d = "변을 하나도 공유하지 않는"
    else: v = n * (n - 4); d = "변을 정확히 하나만 공유하는"
    chk = 0
    for t in itertools.combinations(range(n), 3):
        sh = sum(1 for i in range(3) for j in range(i + 1, 3) if (t[i] - t[j]) % n in (1, n - 1))
        if (kind == "none" and sh == 0) or (kind == "one" and sh == 1): chk += 1
    assert chk == v
    o, ans = num_opts(v, rng)
    return ("경우의 수", 3, "EBS형", f"정{n}각형의 꼭짓점 중 세 개를 이어 만든 삼각형 중에서 정{n}각형과 {d} 삼각형의 개수는?", o, ans,
            f"전체 ₙC₃={math.comb(n,3)}. 변 2개 공유 {n}개, 변 1개 공유 {n}·({n}−4)={n*(n-4)}개. 답 {v}.")
times(t13, 8*MULT, maxtry=3000)

# 14 분할
def t14():
    N = rng.randint(8, 15); pos = rng.choice([True, False])
    lo = 1 if pos else 0
    v = sum(1 for x in range(lo, N + 1) for y in range(x, N + 1) for z in range(y, N + 1) if x + y + z == N)
    o, ans = num_opts(v, rng)
    return ("경우의 수", 3, "모의고사형",
            f"x≤y≤z를 만족시키는 {'자연수' if pos else '음이 아닌 정수'} x, y, z에 대하여 방정식 x+y+z={N}의 해 (x, y, z)의 개수는?", o, ans,
            f"{N}을 {'정확히 3개' if pos else '3개 이하'}의 자연수의 합으로 나타내는 분할의 수와 같다 → {v}.")
times(t14, 7*MULT, maxtry=3000)

# 15 현의 길이
TRI = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17)]
def t15():
    a, b, c = rng.choice(TRI)
    d = rng.choice([1, 2, 3])
    r2 = d * d * c * c + rng.choice([9, 16, 25, 36, 64])
    half2 = r2 - d * d * c * c
    k = d * c * c
    L = 2 * math.isqrt(half2)
    o, ans = num_opts(k, rng, step=c)
    return ("도형의 방정식", 2, "교과서 심화",
            f"원 {gwa('x²+y²='+str(r2))} 직선 {a}x+{b}y=k (k>0)가 만나서 생기는 현의 길이가 {L}일 때, k의 값은?", o, ans,
            f"중심과 직선 사이 거리 d=√({r2}−{half2})={d*c}. k/{c}={d*c} → k={k}.")
times(t15, 7*MULT, maxtry=3000)

# 16 포물선-직선 최소거리
def t16():
    m = rng.choice([1, 2, 3, 4]); c = rng.randint(3, 9)
    # y=x², y=mx−c ; 접점 x=m/2, 거리 = (c − m²/4)/√(m²+1)
    val = F(c) - F(m * m, 4)
    if val <= 0: return None
    q = m * m + 1
    ans = rad(val / q, q)
    wrong = set()
    for dv in [F(1, 2), F(1), F(-1, 2), F(3, 2), F(-1), F(2)]:
        if val + dv > 0: wrong.add(rad((val + dv) / q, q))
    wrong.discard(ans); wrong = sorted(wrong)[:4]
    if len(wrong) < 4: return None
    o = wrong + [ans]; rng.shuffle(o)
    return ("이차함수", 3, "EBS형", f"곡선 y=x² 위의 점과 직선 y={lin(m,-c)} 사이의 거리의 최솟값은?", o, ans,
            f"기울기 {m}인 접선의 접점 x={fr(F(m,2))}. 거리 |{m}·{fr(F(m,2))}−{fr(F(m*m,4))}−{c}|/√{q} = {ans}.")
times(t16, 7*MULT, maxtry=3000)

# 17 내분/외분 PQ
def t17():
    x1, y1, x2, y2 = [rng.randint(-5, 8) for _ in range(4)]
    m, n = rng.choice([(2, 1), (1, 2), (3, 1), (1, 3), (3, 2)])
    P = (F(m * x2 + n * x1, m + n), F(m * y2 + n * y1, m + n))
    Q = (F(m * x2 - n * x1, m - n), F(m * y2 - n * y1, m - n))
    d2 = (P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2
    if d2 == 0 or d2.denominator != 1 and (d2 * 9).denominator != 1: return None
    # 표현: sqrt(d2) = sqrt(num)/den
    num, den = d2.numerator, d2.denominator
    sq = math.isqrt(den)
    if sq * sq != den: return None
    ans = rad(F(1, sq), num)
    alts = sorted({rad(F(1, sq), num + dd) for dd in [-8, -4, 4, 8, 2, -2] if num + dd > 0} - {ans})[:4]
    if len(alts) < 4 or any(int(t.split("√")[1].split("/")[0]) > 60 for t in alts + [ans] if "√" in t): return None
    o = alts + [ans]; rng.shuffle(o)
    return ("도형의 방정식", 2, "모의고사형",
            f"두 점 A({x1},{y1}), B({x2},{y2})에 대하여 선분 AB를 {ro(str(m)+":"+str(n))} 내분하는 점을 P, 외분하는 점을 Q라 할 때, 선분 PQ의 길이는?", o, ans,
            f"P=({fr(P[0])}, {fr(P[1])}), Q=({fr(Q[0])}, {fr(Q[1])}) → PQ={ans}.")
times(t17, 7*MULT, maxtry=3000)

# 18 원 접할 조건
def t18():
    a, b = rng.randint(-5, 5), rng.randint(-5, 5)
    if a == 0 or b == 0 or abs(a) == abs(b): return None
    axis = rng.choice(["x", "y"])
    r = abs(b) if axis == "x" else abs(a)
    k = a * a + b * b - r * r
    eq = f"x²+y²{'+' if -2*a>=0 else '−'}{abs(2*a)}x{'+' if -2*b>=0 else '−'}{abs(2*b)}y+k=0"
    o, ans = num_opts(k, rng)
    return ("도형의 방정식", 2, "모의고사형", f"원 {eq}이 {axis}축에 접할 때, 상수 k의 값은?", o, ans,
            f"중심 ({a},{b}), 반지름² = {a*a+b*b}−k. {axis}축에 접하면 반지름 {r} → k={k}.")
times(t18, 7*MULT, maxtry=3000)

# 19 극선 삼각형 넓이
PAIRS = [(5, 3), (5, 4), (10, 6), (10, 8), (13, 5), (13, 12), (15, 9), (15, 12), (20, 12), (20, 16)]
def t19():
    d, r = rng.choice(PAIRS); t = math.isqrt(d * d - r * r)
    area = F(r * t ** 3, d * d)
    alts = sorted({fr(area * k) for k in [F(1, 2), F(3, 4), F(5, 4), F(3, 2), F(2)]})[:4]
    ans = fr(area); o = alts + [ans]; rng.shuffle(o)
    if not uniq(o): return None
    return ("도형의 방정식", 3, "수능형", f"점 P({d},0)에서 원 x²+y²={r*r}에 그은 두 접선의 접점을 A, B라 할 때, 삼각형 PAB의 넓이는?", o, ans,
            f"PA={t}. 현 AB는 x={fr(F(r*r,d))}, AB={fr(F(2*r*t,d))}, P와의 거리 {fr(F(t*t,d))}. 넓이 {ans}.")
times(t19, 8*MULT, maxtry=3000)

# 20 PA²+PB² 최소
def t20():
    a, b, dd = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (4, 3, 5), (8, 6, 10)])
    r = rng.randint(1, dd - 1); c = rng.randint(1, 4)
    v = 2 * (dd - r) ** 2 + 2 * c * c
    kind = rng.choice(["min", "max"])
    if kind == "max": v = 2 * (dd + r) ** 2 + 2 * c * c
    o, ans = num_opts(v, rng)
    return ("도형의 방정식", 3, "모의고사형",
            f"원 (x−{a})²+(y−{b})²={r*r} 위의 점 P와 두 점 A(−{c},0), B({c},0)에 대하여 PA²+PB²의 {'최솟값' if kind=='min' else '최댓값'}은?", o, ans,
            f"PA²+PB²=2(x²+y²)+{2*c*c}. 원점과 중심 거리 {dd} → OP {'최소 '+str(dd-r) if kind=='min' else '최대 '+str(dd+r)} → {v}.")
times(t20, 8*MULT, maxtry=3000)

# 21 아폴로니우스 원 반지름
def t21():
    p, q = sorted(rng.sample(range(-6, 9), 2)); k = rng.choice([2, 3])
    R = F(k * (q - p), k * k - 1)
    o, ans = num_opts(R, rng)
    return ("도형의 방정식", 3, "EBS형", f"두 점 A({p},0), B({q},0)에 대하여 PA:PB=1:{k}를 만족시키는 점 P가 그리는 원의 반지름의 길이는?", o, ans,
            f"아폴로니우스 원. 1:{k}로 내분점·외분점을 지름의 양 끝으로 갖는다 → 반지름 {k}·{q-p}/({k*k}−1)={ans}.")
times(t21, 8*MULT, maxtry=3000)

# 22 반사 최단경로
def t22():
    x1, y1, x2, y2 = rng.randint(-3, 3), rng.randint(1, 6), rng.randint(3, 9), rng.randint(1, 6)
    d2 = (x2 - x1) ** 2 + (y1 + y2) ** 2
    ans = rad(1, d2)
    alts = sorted({rad(1, d2 + dd) for dd in [-10, -5, 5, 10, 3]} - {ans})[:4]
    if len(alts) < 4: return None
    o = alts + [ans]; rng.shuffle(o)
    return ("도형의 방정식", 2, "교과서 심화", f"두 점 A({x1},{y1}), B({x2},{y2})와 x축 위의 점 P에 대하여 AP+PB의 최솟값은?", o, ans,
            f"B를 x축 대칭한 B′({x2},−{y2}). 최솟값 AB′=√({(x2-x1)**2}+{(y1+y2)**2})={ans}.")
times(t22, 7*MULT, maxtry=3000)

# 23 부분집합 개수
def t23():
    n = rng.randint(8, 12); a = rng.randint(3, 5); g = rng.randint(1, a - 1); k = rng.randint(g + 1, g + n - a - 1)
    v = math.comb(n - a, k - g)
    A = "{" + ",".join(map(str, range(1, a + 1))) + "}"; G = "{" + ",".join(map(str, range(1, g + 1))) + "}"
    o, ans = num_opts(v, rng)
    return ("집합", 2, "모의고사형", f"U={{1,2,…,{n}}}의 부분집합 X 중 {A}∩X={G}이고 n(X)={k}인 X의 개수는?", o, ans,
            f"{G}는 포함, 나머지 {A}의 원소는 제외. 남은 {n-a}개 중 {k-g}개 선택: {v}.")
times(t23, 7*MULT, maxtry=3000)

# 24 충분조건
def t24():
    p, q = sorted(rng.sample(range(-6, 10), 2)); r = rng.randint(1, 3)
    if q - p < 2 * r: return None
    cnt = q - p - 2 * r + 1
    which = rng.choice(["suff", "nec"])
    o, ans = num_opts(cnt, rng, lo=1)
    # q: (x−p)(x−q)≤0
    return ("명제", 2, "모의고사형",
            f"두 조건 p: |x−a|≤{r}, q: {poly_str([1,-(p+q),p*q])}≤0에 대하여 p가 q이기 위한 충분조건이 되도록 하는 정수 a의 개수는?", o, ans,
            f"q: {p}≤x≤{q}. [a−{r}, a+{r}]⊆[{p},{q}] → {p+r}≤a≤{q-r} → {cnt}개.")
times(t24, 7*MULT, maxtry=3000)

# 25 x>c 유리식 최소
def t25():
    c = rng.randint(1, 4); s = rng.randint(1, 5); b = rng.randint(-4, 4)
    d = s * s - c * c - b * c
    v = 2 * s + 2 * c + b
    o, ans = num_opts(v, rng)
    return ("절대부등식", 3, "모의고사형", f"x>{c}일 때, ({poly_str([1,b,d])})/(x−{c})의 최솟값은?", o, ans,
            f"t=x−{c}>0으로 놓으면 t+{s*s}/t+{2*c+b} ≥ 2·{s}+{2*c+b}={v} (t={s}일 때 등호).")
times(t25, 8*MULT, maxtry=3000)

# 26 곱의 최소
def t26():
    a, b, c = rng.randint(1, 4), rng.randint(1, 4), rng.randint(1, 9)
    pr = a * b * c; sq = math.isqrt(pr)
    if sq * sq != pr: return None
    v = 2 * sq + a * b + c
    o, ans = num_opts(v, rng)
    A = "" if a == 1 else str(a); B = "" if b == 1 else str(b); C = "" if c == 1 else str(c)
    return ("절대부등식", 3, "EBS형", f"양수 x, y에 대하여 (x+{a}/y)({B}y+{c}/x)의 최솟값은?", o, ans,
            f"전개: {B}xy+{c}+{a*b}+{a*c}/(xy) ≥ 2√{b*a*c}+{a*b+c}={v}.")
times(t26, 8*MULT, maxtry=3000)

# 27 역함수
def t27():
    p = rng.choice([2, 3, 4, -2]); n = rng.randint(-2, 4); m = rng.randint(-5, 9)
    q = m - p * n
    v = rng.randint(-6, 12)
    # f(f(x)) = p²x + pq + q = v
    x = F(v - p * q - q, p * p)
    o, ans = num_opts(x, rng)
    return ("함수", 3, "모의고사형", f"f(x)={p}x+a에 대하여 f⁻¹({m})={n}일 때, (f∘f)⁻¹({v})의 값은?", o, ans,
            f"f({n})={m} → a={q}. f(f(x))={p*p}x+{p*q+q}={v} → x={ans}.")
times(t27, 8*MULT, maxtry=3000)

# 28 유리함수 대칭점+구간
def t28():
    a, k, c = rng.randint(-3, 4), rng.choice([1, 2, 3, 4, 6]), rng.randint(-3, 2)
    # y = a + k/(x−c)  = (ax − ac + k)/(x − c)
    lo, hi = c + 1, c + rng.randint(2, 4)
    f = lambda x: a + F(k, x - c)
    v = (c + a) + f(lo) + f(hi)
    o, ans = num_opts(v, rng)
    return ("유리함수", 2, "모의고사형",
            f"함수 y=({poly_str([a, -a*c+k])})/({lin(1,-c)})의 그래프가 점 (p,q)에 대하여 대칭이고, {lo}≤x≤{hi}에서 최댓값 M, 최솟값 m이다. p+q+M+m의 값은?", o, ans,
            f"y={a}+{k}/(x−({c})) → (p,q)=({c},{a}). 감소함수 → M=f({lo})={fr(f(lo))}, m=f({hi})={fr(f(hi))}. 합 {ans}.")
times(t28, 8*MULT, maxtry=3000)

# 29 무리함수와 직선
def t29():
    p = rng.randint(-3, 4)
    lo = F(-p); hi = F(1, 4) - p
    ans = f"{fr(lo)}≤k<{fr(hi)}"
    o = [ans, f"{fr(lo)}<k<{fr(hi)}", f"{fr(lo)}≤k≤{fr(hi)}", f"k<{fr(hi)}", f"k≥{fr(lo)}"]
    rng.shuffle(o)
    xs = f"x{'−' if p>=0 else '+'}{abs(p)}".replace("x−0", "x")
    return ("무리함수", 4, "수능형", f"함수 y=√({xs})의 그래프와 직선 y=x+k가 서로 다른 두 점에서 만나도록 하는 실수 k의 값의 범위는?", o, ans,
            f"t=√({xs})≥0: t²−t+{p}+k=0이 서로 다른 음이 아닌 두 근 → D=1−4({p}+k)>0, 두 근의 곱 {p}+k≥0 → {ans}.")
times(t29, 7*MULT, maxtry=3000)

# 30 행렬 케일리-해밀턴형
def t30():
    c = rng.randint(1, 4); n = rng.randint(4, 7)
    A = np.array([[0, 1], [c, 1]])
    P = np.linalg.matrix_power(A, n)
    # A^n = pA + qE → p = P[0,1], q = P[0,0]
    p, q = int(P[0, 1]), int(P[0, 0])
    o, ans = num_opts(p + q, rng)
    sup = "⁴⁵⁶⁷"[n - 4]
    return ("행렬", 4, "수능형", f"A=[[0,1],[{c},1]]에 대하여 A{sup}=pA+qE (E는 단위행렬)일 때, p+q의 값은?", o, ans,
            f"A²=A+{c}E를 반복 적용: A{sup}={p}A+{q}E → {p+q}.")
times(t30, 8*MULT, maxtry=3000)

# 31 행렬 합
def t31():
    k = rng.randint(1, 5); n = rng.randint(5, 12)
    v = 2 * n + k * n * (n + 1) // 2
    o, ans = num_opts(v, rng)
    return ("행렬", 3, "EBS형", f"A=[[1,{k}],[0,1]]일 때, 행렬 A+A²+…+A^{n}의 모든 성분의 합은?".replace("^", "의 ").replace("A의 ", "A^"), o, ans,
            f"Aⁿ=[[1,{k}n],[0,1]]. 합=[[{n},{k*n*(n+1)//2}],[0,{n}]] → {v}.")
times(t31, 8*MULT, maxtry=3000)

# 32 ω 합
def t32():
    N = rng.randint(7, 30)
    w = cmath.exp(2j * math.pi / 3)
    v = sum(1 / (1 + w ** k) for k in range(1, N + 1))
    if abs(v.imag) > 1e-9: return None
    val = F(round(v.real * 2), 2)
    o, ans = num_opts(val, rng, step=F(1, 2))
    return ("이차방정식", 3, "수능형", f"x³=1의 한 허근을 ω라 할 때, Σ(k=1~{N}) 1/(1+ωᵏ)의 값은?", o, ans,
            f"1/(1+ω)=−ω, 1/(1+ω²)=−ω², 1/(1+1)=1/2. 세 항마다 합 3/2 → {ans}.")
times(t32, 8*MULT, maxtry=3000)

# 33 z 거듭제곱
def t33():
    n = rng.randint(100, 3000)
    v = round(2 * math.cos(n * math.pi / 3))
    o = ["−2", "−1", "0", "1", "2"]
    ans = fr(v)
    return ("복소수", 3, "수능형", f"z=(1+√3 i)/2일 때, z^{n}+1/z^{n}의 값은?", o, ans,
            f"z²−z+1=0 → z³=−1, z⁶=1. {n}≡{n%6} (mod 6) → 값 {ans}.")
times(t33, 6*MULT, maxtry=3000)

# 34 구간 최솟값 조건의 a 합
def t34():
    p, q = sorted(rng.sample(range(-2, 5), 2))
    if q - p < 2: return None
    c = rng.randint(2, 9); m = rng.randint(-8, 1)
    sols = set()
    if c - m > 0:
        for s in [1, -1]:
            a2 = c - m; r = math.isqrt(a2)
            if r * r == a2 and p <= s * r <= q: sols.add(F(s * r))
    # a<p: f(p)=p²−2ap+c=m
    if p != 0:
        a = F(p * p + c - m, 2 * p)
        if a < p: sols.add(a)
    if q != 0:
        a = F(q * q + c - m, 2 * q)
        if a > q: sols.add(a)
    if len(sols) < 2: return None
    v = sum(sols)
    o, ans = num_opts(v, rng)
    return ("이차함수", 4, "수능형", f"{p}≤x≤{q}에서 이차함수 f(x)=x²−2ax+{c}의 최솟값이 {m}이 되도록 하는 모든 실수 a의 값의 합은?", o, ans,
            f"꼭짓점 a가 구간 안/왼쪽/오른쪽인 경우로 나누어 풀면 a={', '.join(fr(s) for s in sorted(sols))} → 합 {ans}.")
times(t34, 6*MULT, maxtry=3000)

# 35 두 원의 공통현 (깔끔한 값)
def t35():
    h = rng.randint(2, 6); x0 = rng.randint(1, 5); a = rng.randint(x0 + 1, x0 + 6)
    R1 = x0 * x0 + h * h; R2 = (a - x0) ** 2 + h * h
    v = 2 * h
    o, ans = num_opts(v, rng, step=2, lo=2)
    return ("도형의 방정식", 3, "모의고사형", f"두 원 x²+y²={R1}, (x−{a})²+y²={R2}의 공통현의 길이는?", o, ans,
            f"두 식을 빼면 공통현 x={x0}. 반현 √({R1}−{x0*x0})={h} → 길이 {v}.")
times(t35, 7*MULT, maxtry=3000)


# 36 포함배제 배수
def t36():
    N = rng.choice([100, 120, 150, 200, 250, 300]); a, b, c = rng.choice([(2,3,5),(2,3,7),(3,4,5),(2,5,7),(3,5,7),(4,6,9)])
    kind = rng.choice(["or", "only"])
    if kind == "or":
        v = sum(1 for x in range(1, N+1) if x%a==0 or x%b==0 or x%c==0); d = f"{a} 또는 {b} 또는 {c}의 배수"
    else:
        v = sum(1 for x in range(1, N+1) if x%a==0 and x%b!=0 and x%c!=0); d = f"{a}의 배수이지만 {b}의 배수도 {c}의 배수도 아닌 수"
    o, ans = num_opts(v, rng)
    return ("집합", 3, "모의고사형", f"1부터 {N}까지의 자연수 중 {d}의 개수는?", o, ans, f"포함배제의 원리(각 배수의 개수와 최소공배수의 배수 개수)로 세면 {v}.")
times(t36, 15, maxtry=3000)

# 39 연립부등식 정수해
def t39():
    p, q = sorted(rng.sample(range(-5, 9), 2)); c, d = rng.randint(-3, 6), rng.randint(1, 4)
    xs = [x for x in range(-30, 30) if (x-p)*(x-q) < 0 and abs(x-c) <= d]
    if len(xs) < 1: return None
    kind = rng.choice(["cnt", "sum"])
    v = len(xs) if kind == "cnt" else sum(xs)
    o, ans = num_opts(v, rng)
    return ("부등식", 2, "교과서 심화", f"연립부등식 {poly_str([1,-(p+q),p*q])}<0, {eul("|"+lin(1,-c)+"|≤"+str(d))} 만족시키는 정수 x의 {'개수' if kind=='cnt' else '총합'}는?".replace("|x|", "|x|"),
            o, ans, f"첫째 부등식: {p}<x<{q}, 둘째: {c-d}≤x≤{c+d}. 공통 정수 {', '.join(map(str,xs))} → {v}.")
times(t39, 15, maxtry=3000)

# 40 복소수 근
def t40():
    a, b = rng.randint(-4, 5), rng.randint(1, 5)
    p, q = -2*a, a*a + b*b
    kind = rng.choice(["pq", "p_minus_q"])
    v = p + q if kind == "pq" else p - q
    o, ans = num_opts(v, rng)
    z = f"{a}+{b}i" if a else f"{b}i"
    z = z.replace("+1i", "+i").replace("−", "-")
    return ("복소수", 2, "모의고사형", f"계수가 실수인 이차방정식 x²+px+q=0의 한 근이 {z}일 때, {'p+q' if kind=='pq' else 'p−q'}의 값은?", o, ans,
            f"켤레근 {a}−{b}i도 근. 두 근의 합 {2*a}=−p, 곱 {a*a+b*b}=q → p={p}, q={q} → {v}.")
times(t40, 15, maxtry=3000)

# 42 색칠
def t42():
    k = rng.randint(3, 5); shape = rng.choice(["line", "ring", "star"])
    n = rng.randint(4, 5)
    if shape == "line": edges = [(i, i+1) for i in range(n-1)]; d = f"일렬로 이웃한 {n}개의 영역"
    elif shape == "ring": edges = [(i, (i+1) % n) for i in range(n)]; d = f"고리 모양으로 둘러앉은 {n}개의 영역(처음과 끝도 이웃)"
    else: edges = [(0, i) for i in range(1, n)] + [(i, i+1) for i in range(1, n-1)]; d = f"가운데 영역 1개를 {n-1}개의 영역이 일렬로 둘러싼 부채꼴 모양 {n}개 영역(가운데는 모두와 이웃, 바깥끼리는 차례로 이웃)"
    v = sum(1 for col in itertools.product(range(k), repeat=n) if all(col[a] != col[b] for a, b in edges))
    if v == 0: return None
    o, ans = num_opts(v, rng)
    return ("경우의 수", 3, "수능형", f"{d}을 서로 다른 {k}가지 색으로 칠하려 한다. 이웃한 영역은 서로 다른 색을 칠하고 같은 색을 여러 번 써도 될 때, 칠하는 방법의 수는?", o, ans,
            f"영역을 차례로 칠하며 곱의 법칙(고리형·부채꼴은 처음과 끝이 같은 경우를 나누어 계산)으로 세면 {v}.")
times(t42, 15, maxtry=3000)

if __name__ == "__main__":
    from collections import Counter
    print(len(OUT), Counter(o["unit"] for o in OUT))
    for o in OUT[:3] + OUT[-3:]: print(o["q"], o["opts"], o["ans"])
