import math, itertools, datetime, heapq, random
from collections import deque
from fractions import Fraction as F
from common import fr, num_opts, uniq

rng = random.Random(99)
MULT = 7
OUT = []
def add(unit, lvl, src, q, opts, ans, exp):
    assert ans in opts and uniq(opts) and len(opts) == 5, (q, opts, ans)
    OUT.append(dict(unit=unit, lvl=lvl, src=src, q=q, opts=opts, ans=ans, exp=exp))
def times(t, n, maxtry=500):
    seen = set(); got = 0; k = 0
    while got < n and k < maxtry:
        k += 1; r = t()
        if r is None or r[3] in seen: continue
        seen.add(r[3]); add(*r); got += 1

# 수열
def seq():
    kind = rng.choice(["lin", "sqdiff", "fib", "alt", "tri"])
    if kind == "lin":
        a, b, x = rng.choice([2, 3]), rng.randint(-3, 4), rng.randint(1, 5)
        s = [x]
        for _ in range(5): s.append(a * s[-1] + b)
        e = f"앞 수×{a}{'+' if b>=0 else '−'}{abs(b)}"
        lvl = 2
    elif kind == "sqdiff":
        x, p = rng.randint(1, 9), rng.choice([1, 2])
        s = [x]
        for i in range(1, 6): s.append(s[-1] + (i ** 2 if p == 1 else i ** 3))
        e = "차이가 " + ("제곱수 1, 4, 9, 16, 25" if p == 1 else "세제곱수 1, 8, 27, 64, 125")
        lvl = 3
    elif kind == "fib":
        a, b = rng.randint(1, 5), rng.randint(2, 7)
        s = [a, b]
        for _ in range(4): s.append(s[-1] + s[-2])
        e = "앞의 두 수의 합"; lvl = 2
    elif kind == "alt":
        a, d1, b, r = rng.randint(1, 6), rng.randint(2, 5), rng.randint(1, 4), 2
        odd = [a + d1 * i for i in range(4)]; even = [b * r ** i for i in range(3)]
        s = [odd[0], even[0], odd[1], even[1], odd[2], even[2]]
        nxt = odd[3]
        s.append(nxt)
        e = f"홀수 번째는 {d1}씩 증가, 짝수 번째는 2배 → 다음은 홀수 번째 항 {nxt}"; lvl = 3
    else:
        x, d, dd = rng.randint(1, 6), rng.randint(1, 4), rng.randint(2, 4)
        s = [x]; step = d
        for _ in range(5): s.append(s[-1] + step); step += dd
        e = f"차이가 {d}부터 {dd}씩 커진다"; lvl = 3
    shown, ans = s[:-1], s[-1]
    o, a = num_opts(ans, rng)
    return ("수열 추론", lvl, "수리논리", "규칙에 따라 빈칸에 들어갈 수는?\n" + ", ".join(fr(v) for v in shown) + ", (  )", o, a, e + f" → {a}.")
times(seq, 22*MULT, maxtry=6000)

# 시계 각도
def clock():
    h, m = rng.randint(1, 12), rng.choice(range(5, 60, 5))
    ang = abs(30 * h + F(m, 2) - 6 * m) % 360
    ang = min(ang, 360 - ang)
    if ang == 0: return None
    o = sorted({ang + k * 5 for k in range(-2, 3)})
    pos = rng.randrange(5); o = [ang + (k - pos) * 10 for k in range(5)]
    if min(o) < 0: o = [ang + k * 10 for k in range(5)]
    oo = [fr(v) + "°" for v in o]
    return ("수리 퍼즐", 2, "수리논리", f"{h}시 {m}분일 때 시침과 분침이 이루는 각 중 작은 각의 크기는?", oo, fr(ang) + "°",
            f"분침 {6*m}°, 시침 {30*h % 360}°+{m}×0.5°={fr((30*h + F(m,2)) % 360)}° → 작은 각 {fr(ang)}°.")
times(clock, 8*MULT, maxtry=6000)

# 요일
DAYS = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
def weekday():
    y = rng.choice([2025, 2026, 2027])
    d0 = datetime.date(y, 1, 1)
    d1 = d0 + datetime.timedelta(days=rng.randint(40, 360))
    diff = (d1 - d0).days
    ans = DAYS[d1.weekday()]
    i = d1.weekday(); o = [DAYS[(i + k) % 7] for k in range(-2, 3)]; rng.shuffle(o)
    return ("수리 퍼즐", 2, "수리논리", f"{y}년 1월 1일은 {DAYS[d0.weekday()]}이다. {y}년 {d1.month}월 {d1.day}일은 무슨 요일인가?", o, ans,
            f"1월 1일로부터 {diff}일 후. {diff}=7×{diff//7}+{diff%7} → {DAYS[d0.weekday()]}에서 {diff%7}일 뒤 {ans}.")
times(weekday, 8*MULT, maxtry=6000)

# 비둘기집
def pigeon():
    cols = ["빨간", "파란", "초록", "노란"]
    k = rng.choice([3, 4]); cnt = [rng.randint(3, 10) for _ in range(k)]
    kind = rng.choice(["same", "target"])
    names = cols[:k]
    desc = ", ".join(f"{n} 공 {c}개" for n, c in zip(names, cnt))
    if kind == "same":
        need = rng.randint(2, min(cnt))
        v = sum(min(c, need - 1) for c in cnt) + 1
        q = f"상자에 {desc}가 들어 있다. 보지 않고 꺼낼 때, 같은 색 공을 반드시 {need}개 이상 얻으려면 최소 몇 개를 꺼내야 하는가?"
        e = f"최악은 각 색을 {need-1}개씩(그 색이 부족하면 전부) 꺼낸 경우 {v-1}개. 하나 더 꺼내면 반드시 성립 → {v}."
    else:
        t = rng.randrange(k); need = rng.randint(2, cnt[t])
        v = sum(cnt) - cnt[t] + need
        q = f"상자에 {desc}가 들어 있다. 보지 않고 꺼낼 때, {names[t]} 공을 반드시 {need}개 이상 얻으려면 최소 몇 개를 꺼내야 하는가?"
        e = f"최악은 다른 색 {sum(cnt)-cnt[t]}개를 먼저 모두 꺼내는 경우 → {sum(cnt)-cnt[t]}+{need}={v}."
    o, a = num_opts(v, rng)
    return ("최악의 경우", 3, "수리논리", q, o, a, e)
times(pigeon, 8*MULT, maxtry=6000)

# 계단
def stairs():
    n = rng.randint(7, 13); steps = rng.choice([(1, 2), (1, 3), (1, 2, 3)])
    w = [1] + [0] * n
    for i in range(1, n + 1): w[i] = sum(w[i - s] for s in steps if i - s >= 0)
    o, a = num_opts(w[n], rng)
    st = " 또는 ".join(f"{s}칸" for s in steps)
    return ("경우의 수", 3, "수리논리", f"{n}칸 계단을 한 번에 {st}씩 올라갈 때, 올라가는 방법의 수는?", o, a,
            "a(n)=" + "+".join(f"a(n−{s})" for s in steps) + f" 점화식으로 계산하면 a({n})={w[n]}.")
times(stairs, 7*MULT, maxtry=6000)

# 격자
def grid():
    W, H = rng.randint(3, 6), rng.randint(2, 5)
    px, py = rng.randint(1, W - 1), rng.randint(1, H - 1)
    tot = math.comb(W + H, W); thr = math.comb(px + py, px) * math.comb(W - px + H - py, W - px)
    kind = rng.choice(["avoid", "through"])
    v = tot - thr if kind == "avoid" else thr
    o, a = num_opts(v, rng)
    return ("경우의 수", 3, "수리논리",
            f"가로 {W}칸, 세로 {H}칸인 바둑판 모양 도로에서 왼쪽 아래 꼭짓점에서 오른쪽 위 꼭짓점까지 최단 경로로 갈 때, 왼쪽 아래로부터 (가로 {px}, 세로 {py}) 위치의 교차점을 {'지나지 않는' if kind=='avoid' else '반드시 지나는'} 경로의 수는?",
            o, a, f"전체 {tot}, 그 점을 지나는 경로 {math.comb(px+py,px)}×{math.comb(W-px+H-py,W-px)}={thr} → {v}.")
times(grid, 8*MULT, maxtry=6000)

# 님
def nim():
    k = rng.choice([2, 3, 4, 5]); N = rng.randint(15, 40)
    r = N % (k + 1)
    if r == 0: return None
    o = [f"{i}개" for i in range(1, k + 1)] + ["어떻게 해도 진다"]
    while len(o) < 5: o.append(["상관없다", "처음엔 가져가지 않는다"][len(o) - k - 1])
    o = o[:5]
    if f"{r}개" not in o: return None
    return ("게임 전략", 3, "퍼즐", f"돌 {N}개에서 두 사람이 번갈아 1~{k}개씩 가져가고, 마지막 돌을 가져가는 사람이 이긴다. 먼저 하는 사람이 반드시 이기려면 처음에 몇 개를 가져가야 하는가?",
            o, f"{r}개", f"상대에게 항상 {k+1}의 배수를 남기면 이긴다. {N}={k+1}×{N//(k+1)}+{r} → {r}개.")
times(nim, 7*MULT, maxtry=6000)

# 일률
def work():
    a, b = rng.choice([(6, 12), (4, 12), (10, 15), (6, 10), (12, 24), (8, 24), (9, 18), (5, 20)])
    t = rng.randint(1, 2)
    together = F(1, a) + F(1, b)
    rest = 1 - t * together
    if rest <= 0: return None
    tb = rest * b
    total = t + tb
    if total.denominator != 1: return None
    o, ans = num_opts(total, rng)
    return ("방정식 응용", 3, "수리논리", f"A 혼자 하면 {a}일, B 혼자 하면 {b}일 걸리는 일이 있다. 둘이 함께 {t}일 일한 뒤 나머지는 B 혼자 했다. 일을 끝내는 데 걸린 총 일수는?",
            [x + "일" for x in o], ans + "일", f"함께 하루 {fr(together)} → {t}일에 {fr(t*together)}. 남은 {fr(rest)}을 B가 {fr(tb)}일 → 총 {ans}일.")
times(work, 7*MULT, maxtry=6000)

# 나이
def age():
    s = rng.randint(6, 18); k1 = rng.choice([3, 4, 5]); f = k1 * s
    for y in range(1, 40):
        if (f + y) == 2 * (s + y): break
    else: return None
    kind = rng.choice(["sum", "father"])
    v = f + s if kind == "sum" else f
    o, a = num_opts(v, rng)
    return ("방정식 응용", 2, "수리논리", f"현재 아버지의 나이는 아들의 {k1}배이고, {y}년 후에는 2배가 된다. 현재 {'두 사람 나이의 합은' if kind=='sum' else '아버지의 나이는'}?",
            o, a, f"{k1}x+{y}=2(x+{y}) → x={s}, 아버지 {f} → {v}.")
times(age, 6*MULT, maxtry=6000)

# 큐브
def cube():
    n = rng.randint(3, 7); k = rng.choice([0, 1, 2])
    v = {3: 8, 2: 12 * (n - 2), 1: 6 * (n - 2) ** 2, 0: (n - 2) ** 3}[k]
    e = {3: "꼭짓점 8개", 2: f"모서리 12개×({n}−2)", 1: f"면 6개×({n}−2)²", 0: f"내부 ({n}−2)³"}[k]
    o, a = num_opts(v, rng)
    kk = "하나도 칠해지지 않은" if k == 0 else f"정확히 {k}면만 칠해진"
    return ("공간 지각", 3, "수리논리", f"겉면을 모두 칠한 정육면체를 {n}×{n}×{n}개의 작은 정육면체로 잘랐다. {kk} 작은 정육면체의 개수는?", o, a, f"{e} = {v}.")
times(cube, 8*MULT, maxtry=6000)

# 다리 건너기
def bridge_opt(ts):
    start = (frozenset(range(len(ts))), 0)
    dist = {start: 0}; pq = [(0, 0, start)]; cnt = 0
    while pq:
        d, _, (left, side) = heapq.heappop(pq)
        if not left: return d
        if d > dist[(left, side)]: continue
        if side == 0:
            moves = [frozenset(c) for c in itertools.combinations(left, 2)] + ([frozenset(left)] if len(left) == 1 else [])
            for mv in moves:
                ns = (left - mv, 1); nd = d + max(ts[i] for i in mv)
                if nd < dist.get(ns, 1e9): dist[ns] = nd; cnt += 1; heapq.heappush(pq, (nd, cnt, ns))
        else:
            right = frozenset(range(len(ts))) - left
            for i in right:
                ns = (left | {i}, 0); nd = d + ts[i]
                if nd < dist.get(ns, 1e9): dist[ns] = nd; cnt += 1; heapq.heappush(pq, (nd, cnt, ns))
def bridge():
    n = rng.choice([4, 4, 5]); ts = sorted(rng.sample(range(1, 16), n))
    v = bridge_opt(ts)
    naive = sum(ts[1:]) + ts[0] * (n - 2)
    o, a = num_opts(v, rng)
    return ("최적화", 4, "퍼즐", f"밤에 손전등 1개로 다리를 건넌다. 한 번에 최대 2명, 손전등이 꼭 필요하고 둘이 건너면 느린 사람 속도로 간다. 건너는 데 각각 {', '.join(map(str,ts))}분 걸리는 {n}명이 모두 건너는 최소 시간은?",
            [x + "분" for x in o], a + "분",
            f"가장 빠른 사람이 계속 왕복하면 {naive}분. 가장 느린 두 명을 함께 보내고 빠른 두 명이 손전등을 나르는 전략을 섞으면 최소 {v}분.")
times(bridge, 6*MULT, maxtry=6000)

# 물통
def jugs():
    A, B = rng.choice([(3, 5), (4, 7), (3, 7), (5, 8), (4, 9), (2, 7)]); T = rng.randint(1, B - 1)
    if T in (A, B): return None
    start = (0, 0); seen = {start: 0}; q = deque([start]); ans = None
    while q:
        a, b = q.popleft()
        if a == T or b == T: ans = seen[(a, b)]; break
        nx = [(A, b), (a, B), (0, b), (a, 0)]
        t = min(a, B - b); nx.append((a - t, b + t)); t = min(b, A - a); nx.append((a + t, b - t))
        for n in nx:
            if n not in seen: seen[n] = seen[(a, b)] + 1; q.append(n)
    if ans is None or ans < 3: return None
    o, a = num_opts(ans, rng, lo=1)
    return ("최적화", 3, "퍼즐", f"{A} L 통과 {B} L 통, 무제한 물로 정확히 {T} L를 만들려 한다. '채우기·비우기·옮겨 붓기'를 각각 1회 조작으로 셀 때 최소 조작 횟수는?",
            [x + "회" for x in o], a + "회", f"가능한 상태를 모두 탐색(너비 우선)하면 최소 {ans}회에 처음으로 {T} L가 만들어진다.")
times(jugs, 6*MULT, maxtry=6000)

# 기사와 건달 (자동 생성 + 유일 결론)
NAMES = ["A", "B", "C"]
def knights():
    stmts = []
    def mk():
        k = rng.choice(["is_knave", "same", "diff", "atleast1knave", "both_knights"])
        i = rng.randrange(3); j = rng.choice([x for x in range(3)])
        others = [x for x in range(3) if x != i]
        if k == "is_knave": j = rng.choice(others); return (k, j), f"{NAMES[j]}는 건달이다.", lambda w: not w[j]
        if k == "same": a, b = others; return (k, a, b), f"{NAMES[a]}와 {NAMES[b]}는 같은 부류다.", lambda w: w[a] == w[b]
        if k == "diff": a, b = others; return (k, a, b), f"{NAMES[a]}와 {NAMES[b]}는 다른 부류다.", lambda w: w[a] != w[b]
        if k == "atleast1knave": return (k,), "우리 셋 중 적어도 한 명은 건달이다.", lambda w: not all(w)
        return (k,), "우리 셋은 모두 기사다.", lambda w: all(w)
    sp = []
    for s in range(2): sp.append(mk())
    speakers = rng.sample(range(3), 2)
    sols = [w for w in itertools.product([True, False], repeat=3) if all(w[speakers[t]] == sp[t][2](w) for t in range(2))]
    if not sols: return None
    facts = []
    for i in range(3):
        vals = {w[i] for w in sols}
        if len(vals) == 1: facts.append(f"{NAMES[i]}는 {'기사' if vals.pop() else '건달'}이다.")
    if len(facts) != 1 and len(sols) != 1: return None
    if len(sols) == 1:
        w = sols[0]; ans = ", ".join(f"{NAMES[i]} {'기사' if w[i] else '건달'}" for i in range(3))
        allw = [", ".join(f"{NAMES[i]} {'기사' if w2[i] else '건달'}" for i in range(3)) for w2 in itertools.product([True, False], repeat=3)]
        o = [ans] + rng.sample([x for x in allw if x != ans], 4); rng.shuffle(o)
        qq = "세 사람의 정체를 바르게 짝지은 것은?"
    else:
        ans = facts[0]
        pool = [f"{n}는 {t}이다." for n in NAMES for t in ["기사", "건달"] if f"{n}는 {t}이다." != ans]
        # 거짓/불확정 진술만 오답으로
        o = [ans] + rng.sample(pool, 4); rng.shuffle(o)
        qq = "반드시 참인 것은?"
    text = " ".join(f"{NAMES[speakers[t]]}: \"{sp[t][1]}\"" for t in range(2))
    return ("논리 퍼즐", 4 if len(sols) == 1 else 3, "PSAT형",
            f"섬에는 진실만 말하는 기사와 거짓만 말하는 건달만 산다. {text} {qq}", o, ans,
            f"8가지 경우를 모두 따져 보면 두 발언과 모순되지 않는 경우는 {len(sols)}가지이고, 공통 결론은 '{ans}'.")
times(knights, 7*MULT, maxtry=6000)


# 비밀번호 추리 (유일해 보장)
def score(code, guess):
    right = sum(c == g for c, g in zip(code, guess))
    common = sum(min(code.count(d), guess.count(d)) for d in set(guess))
    return right, common - right
ALLC = ["".join(p) for p in itertools.permutations("0123456789", 3)]
def desc(r):
    a, b = r
    if a == 0 and b == 0: return "맞는 숫자가 없다."
    parts = []
    if a: parts.append(f"숫자 {a}개는 위치까지 맞다")
    if b: parts.append(f"숫자 {b}개는 맞지만 위치가 틀리다")
    return ", ".join(parts) + "."
def password():
    code = rng.choice(ALLC); clues = []; cand = ALLC
    for _ in range(8):
        g = rng.choice(ALLC)
        r = score(code, g)
        if r == (3, 0): continue
        clues.append((g, r)); cand = [c for c in cand if score(c, g) == r]
        if len(cand) == 1: break
    if len(cand) != 1 or len(clues) < 4: return None
    wrong = set()
    for c in ALLC:
        if c != code and sum(a == b for a, b in zip(c, code)) >= 1 and set(c) & set(code): wrong.add(c)
    o = [code] + rng.sample(sorted(wrong), 4); rng.shuffle(o)
    lines = "\n".join(f"· {g}: {desc(r)}" for g, r in clues)
    return ("논리 퍼즐", 4, "퍼즐", "서로 다른 숫자 3개로 된 비밀번호에 대한 힌트이다. 비밀번호는?\n" + lines, o, code,
            f"힌트를 모두 만족하는 서로 다른 세 숫자의 배열은 {code} 하나뿐이다. (맞는 숫자가 없는 힌트로 후보를 먼저 지우면 빠르다.)")
times(password, 110, maxtry=20000)

# 자리 배치 (유일해 보장)
PEOPLE = ["진우", "민준", "서연", "하린", "도윤"]
def _bat(w): return (ord(w[-1]) - 0xAC00) % 28 != 0
def nn(w): return w + ("은" if _bat(w) else "는")
def wg(w): return w + ("과" if _bat(w) else "와")
def seating():
    n = 5; arr = rng.sample(PEOPLE, n); pos = {p: i for i, p in enumerate(arr)}
    pool = []
    for a in PEOPLE:
        for b in PEOPLE:
            if a == b: continue
            if pos[b] == pos[a] + 1: pool.append((f"{nn(b)} {a}의 바로 오른쪽에 앉는다.", lambda P, a=a, b=b: P[b] == P[a] + 1))
            if abs(pos[a] - pos[b]) > 1 and a < b: pool.append((f"{wg(a)} {nn(b)} 이웃하지 않는다.", lambda P, a=a, b=b: abs(P[a] - P[b]) > 1))
            if pos[a] < pos[b] and a < b: pool.append((f"{nn(a)} {b}보다 왼쪽에 앉는다.", lambda P, a=a, b=b: P[a] < P[b]))
        if pos[a] in (0, n - 1): pool.append((f"{nn(a)} 양 끝 중 한 자리에 앉는다.", lambda P, a=a: P[a] in (0, n - 1)))
        else: pool.append((f"{nn(a)} 양 끝에 앉지 않는다.", lambda P, a=a: P[a] not in (0, n - 1)))
    rng.shuffle(pool); chosen = []
    perms = list(itertools.permutations(PEOPLE))
    cand = perms
    for text, f in pool:
        newc = [p for p in cand if f({x: i for i, x in enumerate(p)})]
        if len(newc) < len(cand): chosen.append(text); cand = newc
        if len(cand) == 1: break
    if len(cand) != 1 or not (4 <= len(chosen) <= 7): return None
    k = rng.randrange(n); ans = arr[k]
    o = PEOPLE[:]; rng.shuffle(o)
    place = ["맨 왼쪽", "왼쪽에서 두 번째", "가운데", "오른쪽에서 두 번째", "맨 오른쪽"][k]
    return ("논리 퍼즐", 4, "PSAT형", "다섯 명이 일렬로 앉는다. 다음 조건을 모두 만족할 때 " + place + " 자리에 앉은 사람은?\n" + "\n".join("· " + c for c in chosen),
            o, ans, "조건을 모두 만족하는 배치는 " + " - ".join(arr) + " 하나뿐이다.")
times(seating, 120, maxtry=20000)

# 범인 찾기 (거짓말쟁이 수 지정, 유일해)
SUS = ["A", "B", "C", "D", "E"]
def culprit():
    stmts = []
    for sp in SUS:
        k = rng.choice(["is", "isnot", "self", "or"])
        if k == "is": t = rng.choice(SUS); stmts.append((sp, f"범인은 {t}다.", lambda X, t=t: X == t))
        elif k == "isnot": t = rng.choice([x for x in SUS if x != sp]); stmts.append((sp, f"{t}는 범인이 아니다.", lambda X, t=t: X != t))
        elif k == "self": stmts.append((sp, "나는 범인이 아니다.", lambda X, sp=sp: X != sp))
        else:
            t1, t2 = rng.sample(SUS, 2); stmts.append((sp, f"범인은 {t1} 또는 {t2}다.", lambda X, t1=t1, t2=t2: X in (t1, t2)))
    L = rng.choice([1, 1, 2, 4])
    sols = [X for X in SUS if sum(1 for _, _, f in stmts if not f(X)) == L]
    if len(sols) != 1: return None
    X = sols[0]; o = SUS[:]
    lines = "\n".join(f"{sp}: {t}" for sp, t, _ in stmts)
    rule = {1: "정확히 1명만 거짓말을 한다", 2: "정확히 2명이 거짓말을 한다", 4: "정확히 1명만 진실을 말한다"}[L]
    liars = [sp for sp, _, f in stmts if not f(X)]
    return ("논리 퍼즐", 4, "PSAT형", f"범인은 A~E 중 1명이고, 다섯 명 중 {rule}. 범인은?\n" + lines, o, X,
            f"범인을 A~E로 하나씩 가정해 거짓말한 사람 수를 세면 조건을 만족하는 경우는 범인 {X}일 때뿐이다(거짓말: {', '.join(liars)}).")
times(culprit, 120, maxtry=20000)

if __name__ == "__main__":
    from collections import Counter
    print(len(OUT), Counter(o["unit"] for o in OUT))
    for o in OUT[::9]: print(o["q"], o["opts"], o["ans"], "|", o["exp"])
