"""그래프·도형형 + 사례형 고난도 수학 문항 생성기 (그림 SVG 포함, 정답은 코드로 계산·검증)"""
import math, itertools, random
from fractions import Fraction as F
from common import fr, rad, num_opts, uniq
import gen_math as G
import svgfig as S

rng = random.Random(2027)
OUT = []
P = G.poly_str; L = G.lin
def LF(m, n):
    m, n = F(m), F(n)
    if m == 0: xs = ""
    elif m == 1: xs = "x"
    elif m == -1: xs = "−x"
    elif m.denominator == 1: xs = fr(m) + "x"
    else: xs = ("−" if m < 0 else "") + f"({fr(abs(m))})x"
    if n == 0: return xs or "0"
    ns = fr(abs(n))
    if not xs: return fr(n)
    return xs + ("+" if n > 0 else "−") + ns
def add(unit, lvl, src, q, opts, ans, exp, fig=""):
    q, exp = G._clean(q), G._clean(exp)
    opts = [G._clean(o) for o in opts]; ans = G._clean(ans)
    import re as _re
    fig = _re.sub(r'(<text[^>]*>)([^<]*)', lambda m: m.group(1) + m.group(2).replace('-', '−'), fig)
    assert ans in opts and uniq(opts) and len(opts) == 5, (q, opts, ans)
    OUT.append(dict(unit=unit, lvl=lvl, src=src, q=q, opts=opts, ans=ans, exp=exp, fig=fig))
def times(t, n, maxtry=6000):
    seen = set(); got = 0; k = 0
    while got < n and k < maxtry:
        k += 1; r = t()
        if r is None: continue
        key = r[3] + (r[7] if len(r) > 7 else '') + '|'.join(map(str, r[4]))
        if key in seen: continue
        seen.add(key); add(*r); got += 1

# ===================== 그래프·도형형 =====================

# F1 이차함수 그래프 읽기 → 계수
def f1():
    r1, r2 = sorted(rng.sample(range(-4, 6), 2)); a = rng.choice([1, -1, F(1, 2), -F(1, 2), 2])
    f = lambda x: float(a * (x - r1) * (x - r2))
    c = a * r1 * r2; b = -a * (r1 + r2)
    if c == 0: return None
    vx = F(r1 + r2, 2); vy = a * (vx - r1) * (vx - r2)
    ys = [0, float(c), float(vy)]
    pl = S.Plane(min(-5, r1 - 1), max(6, r2 + 1), min(ys) - 2, max(ys) + 2).axes()
    pl.curve(f).pt((r1, 0), str(r1), -4, 16).pt((r2, 0), str(r2), -4, 16).pt((0, float(c)), fr(c), 6, -4)
    kind = rng.choice(["abc", "vertex", "f_at"])
    if kind == "abc": v = a + b + c; w = "a+b+c"; e = f"y=a(x−({r1}))(x−({r2}))에 (0,{fr(c)}) 대입 → a={fr(a)}. a+b+c=f(1)={fr(v)}"
    elif kind == "vertex": v = vy; w = "꼭짓점의 y좌표"; e = f"a={fr(a)}, 축 x={fr(vx)} → 꼭짓점 y좌표 {fr(v)}"
    else:
        x0 = rng.choice([x for x in range(-3, 6) if x not in (r1, r2, 0)]); v = a * (x0 - r1) * (x0 - r2); w = f"f({x0})의 값"; e = f"f(x)={fr(a)}(x−{r1})(x−{r2}) → f({x0})={fr(v)}"
    o, ans = num_opts(v, rng)
    return ("이차함수", 3, "그래프 해석", f"그림은 이차함수 y=f(x)=ax²+bx+c의 그래프이다. 그래프가 x축과 x={r1}, x={r2}에서 만나고 y축과 y={fr(c)}에서 만날 때, {w}는?", o, ans, e + ".", pl.svg())
times(f1, 30)

# F2 포물선과 직선, 교점과 원점이 이루는 삼각형 넓이
def f2():
    x1, x2 = sorted(rng.sample(range(-3, 5), 2)); k = rng.choice([1, F(1, 2)])
    # y=k x² 와 직선이 x1,x2에서 만남 → 직선 y=k(x1+x2)x − k x1 x2
    m = k * (x1 + x2); n = -k * x1 * x2
    if n == 0: return None
    A = (x1, k * x1 * x1); B = (x2, k * x2 * x2)
    area = abs(A[0] * B[1] - B[0] * A[1]) / 2
    pl = S.Plane(min(-4, x1 - 1), max(5, x2 + 1), -2, float(max(A[1], B[1])) + 2).axes()
    pl.poly([(0, 0), (float(A[0]), float(A[1])), (float(B[0]), float(B[1]))]).curve(lambda x: float(k) * x * x).line((pl.x0, float(m) * pl.x0 + float(n)), (pl.x1, float(m) * pl.x1 + float(n)))
    pl.pt((float(A[0]), float(A[1])), "A", -14).pt((float(B[0]), float(B[1])), "B")
    o, ans = num_opts(area, rng)
    ks = "" if k == 1 else "½"
    return ("이차함수", 4, "그래프 해석", f"그림과 같이 곡선 y={ks}x²과 직선 y={LF(m, n)}이 두 점 A, B에서 만난다. 원점 O에 대하여 삼각형 OAB의 넓이는?", o, ans,
            f"{ks}x²={LF(m,n)} → x={x1}, {x2}. A({x1},{fr(A[1])}), B({x2},{fr(B[1])}). 넓이=½|x₁y₂−x₂y₁|={fr(area)}.", pl.svg())
times(f2, 26)

# F3 원 밖의 점에서 그은 접선 – 사각형 넓이/접선 길이
PAIRS = [(5, 3), (5, 4), (10, 6), (10, 8), (13, 5), (13, 12)]
def f3():
    d, r = rng.choice(PAIRS); t = int(math.isqrt(d * d - r * r)); cx, cy = rng.randint(-2, 2), rng.randint(-2, 2)
    # P 방향: x축 방향으로 d
    P_ = (cx + d, cy)
    kind = rng.choice(["quad", "len", "chord"])
    if kind == "quad": v = F(r * t); w = "사각형 CAPB의 넓이"; e = f"PA=√({d}²−{r}²)={t}, 넓이=2×½×{r}×{t}={r*t}"
    elif kind == "len": v = F(t); w = "선분 PA의 길이"; e = f"PA=√(CP²−r²)=√({d*d}−{r*r})={t}"
    else: v = F(2 * r * t, d); w = "선분 AB의 길이"; e = f"AB=2·(r·PA/CP)=2·{r}·{t}/{d}={fr(v)}"
    s = 1.0
    xa = cx + r * r / d; ya = r * t / d
    pl = S.Plane(min(cx - r - 2, -1), cx + d + 2, min(cy - r - 2, -1), max(cy + r + 2, 1), equal=True).axes()
    pl.circle((cx, cy), r).line(P_, (xa, cy + ya)).line(P_, (xa, cy - ya)).line((cx, cy), (xa, cy + ya), "c3").line((cx, cy), (xa, cy - ya), "c3")
    pl.pt((cx, cy), "C").pt(P_, "P").pt((xa, cy + ya), "A").pt((xa, cy - ya), "B", 6, 14)
    o, ans = num_opts(v, rng)
    return ("도형의 방정식", 3, "도형 해석", f"그림과 같이 원 {('x' if cx==0 else '(x−'+str(cx)+')')}²+{('y' if cy==0 else '(y−'+str(cy)+')')}²={r*r}의 중심을 C라 하고, 점 P({cx+d},{cy})에서 원에 그은 두 접선의 접점을 A, B라 하자. {w}는?".replace("x−-", "x+").replace("y−-", "y+"), o, ans, e + ".", pl.svg())
times(f3, 26)

# F4 원 위의 점과 직선 사이 거리 최대·최소 → 삼각형 넓이 최대
def f4():
    a, b, c = rng.choice([(3, 4, 5), (4, 3, 5), (5, 12, 13), (12, 5, 13), (6, 8, 10)]); k = c * rng.randint(2, 4); r = rng.randint(1, 3)
    # 직선 ax+by=k, 원 x²+y²=r², 직선과 축의 교점 A(k/a,0), B(0,k/b)
    A_ = (F(k, a), F(0)); B_ = (F(0), F(k, b)); AB = F(k, a * b) * c  # 길이
    dist = F(k, c)
    kind = rng.choice(["max", "min"])
    h = dist + r if kind == "max" else dist - r
    if h <= 0: return None
    area = AB * h / 2
    if area.denominator > 10: return None
    pl = S.Plane(-r - 1.5, float(A_[0]) + 1.5, -r - 1.5, float(B_[1]) + 1.5, equal=True).axes()
    pl.circle((0, 0), r).line((float(A_[0]), 0), (0, float(B_[1]))).pt((float(A_[0]), 0), "A", -4, 16).pt((0, float(B_[1])), "B", 6, 4)
    o, ans = num_opts(area, rng)
    return ("도형의 방정식", 4, "도형 해석", f"그림과 같이 직선 {a}x+{b}y={k}가 x축, y축과 만나는 점을 각각 A, B라 하자. 원 x²+y²={r*r} 위의 점 P에 대하여 삼각형 ABP의 넓이의 {'최댓값' if kind=='max' else '최솟값'}은?", o, ans,
            f"AB={fr(AB)}, 원점과 직선 거리 {fr(dist)} → P와 직선 거리 {'최대 '+fr(dist)+'+'+str(r) if kind=='max' else '최소 '+fr(dist)+'−'+str(r)}={fr(h)}. 넓이 ½·{fr(AB)}·{fr(h)}={fr(area)}.", pl.svg())
times(f4, 24)

# F5 삼각형 — 무게중심·넓이 이등분
def f5():
    pts = [(rng.randint(-4, 1), rng.randint(-3, 1)), (rng.randint(2, 6), rng.randint(-3, 2)), (rng.randint(-2, 4), rng.randint(3, 6))]
    (ax, ay), (bx, by), (cx_, cy_) = pts
    if (0, 0) in pts: return None
    area2 = abs((bx - ax) * (cy_ - ay) - (cx_ - ax) * (by - ay))
    if area2 == 0: return None
    kind = rng.choice(["area", "centroid", "median"])
    if kind == "area": v = F(area2, 2); w = "삼각형 ABC의 넓이"; e = f"신발끈 공식: ½|…|={fr(v)}"
    elif kind == "centroid": gx, gy = F(ax + bx + cx_, 3), F(ay + by + cy_, 3); v = gx + gy; w = "무게중심 G의 x좌표와 y좌표의 합"; e = f"G=({fr(gx)}, {fr(gy)}) → {fr(v)}"
    else:
        mx, my = F(bx + cx_, 2), F(by + cy_, 2)
        if mx == ax: return None
        v = (my - ay) / (mx - ax); w = "점 A를 지나고 삼각형 ABC의 넓이를 이등분하는 직선의 기울기"; e = f"BC의 중점 M({fr(mx)},{fr(my)})을 지나야 한다 → 기울기 {fr(v)}"
    pl = S.Plane(-5, 7, -4, 7).axes()
    pl.poly(pts).pt(pts[0], "A", -14, 12).pt(pts[1], "B", 6, 12).pt(pts[2], "C")
    o, ans = num_opts(v, rng)
    return ("도형의 방정식", 3, "도형 해석", f"그림과 같이 세 점 A({ax},{ay}), B({bx},{by}), C({cx_},{cy_})를 꼭짓점으로 하는 삼각형 ABC가 있다. {w}는?", o, ans, e + ".", pl.svg())
times(f5, 26)

# F6 유리함수 그래프 읽기
def f6():
    p, q, k = rng.randint(-3, 3), rng.randint(-3, 3), rng.choice([1, 2, 3, 4, -1, -2, -3, 6])
    x0 = rng.choice([x for x in range(-4, 6) if x != p and k % (x - p) == 0]) if any(k % (x - p) == 0 for x in range(-4, 6) if x != p) else None
    if x0 is None: return None
    y0 = q + F(k, x0 - p)
    f = lambda x: q + k / (x - p)
    pl = S.Plane(p - 6, p + 6, q - 6, q + 6).axes()
    pl.vline(p).hline(q).curve(f, p - 6, p - 0.02).curve(f, p + 0.02, p + 6).pt((x0, float(y0)), f"({x0}, {fr(y0)})", 6, -6)
    pl.text((p, q - 6), f"x={p}", 4, -4).text((p + 6, q), f"y={q}", -30, -6)
    # y=(ax+b)/(x+c) → a=q, c=−p, b=k−pq
    a_, b_, c_ = q, k - p * q, -p
    v = a_ + b_ + c_
    o, ans = num_opts(v, rng)
    return ("유리함수", 4, "그래프 해석", f"그림은 함수 y=(ax+b)/(x+c)의 그래프와 두 점근선 x={p}, y={q}를 나타낸 것이다. 그래프가 점 ({x0}, {fr(y0)})을 지날 때, a+b+c의 값은?", o, ans,
            f"y={q}+k/(x−({p}))에 점을 대입하면 k={k}. 정리하면 y=({P([a_, b_]) if a_ else b_})/({L(1, c_)}) → a={a_}, b={b_}, c={c_}, a+b+c={v}.", pl.svg())
times(f6, 26)

# F7 무리함수 그래프 읽기
def f7():
    p, q, a = rng.randint(-3, 3), rng.randint(-3, 3), rng.choice([1, 2, 3, 4])
    t = rng.randint(1, 3); x1 = p + F(t * t, a)
    if x1.denominator != 1: return None
    f = lambda x: q + math.sqrt(a * (x - p)) if x >= p else None
    pl = S.Plane(p - 2, p + 9, q - 2, q + 6).axes()
    pl.curve(f, p, p + 9).pt((p, q), f"({p}, {q})", 6, 14).pt((float(x1), q + t), f"({fr(x1)}, {q+t})", 6, -6)
    v = a + p + q
    o, ans = num_opts(v, rng)
    return ("무리함수", 4, "그래프 해석", f"그림은 함수 y=√(a(x−p))+q의 그래프이다. 그래프의 시작점이 ({p}, {q})이고 점 ({fr(x1)}, {q+t})를 지날 때, a+p+q의 값은?", o, ans,
            f"시작점 → p={p}, q={q}. √(a·{fr(x1-p)})={t} → a={a}. 합 {v}.", pl.svg())
times(f7, 26)

# F8 벤다이어그램
def f8():
    a, ab, b, out = [rng.randint(2, 15) for _ in range(4)]
    U = a + ab + b + out
    kind = rng.choice(["union", "only", "sym", "comp"])
    shown = {"a": "x", "ab": ab, "b": b, "out": out}
    nA = a + ab
    if kind == "union": v = a + ab + b; w = "n(A∪B)"
    elif kind == "only": v = a; w = "n(A−B)"
    elif kind == "sym": v = a + b; w = "n((A−B)∪(B−A))"
    else: v = b + out; w = "n(Aᶜ)"
    o, ans = num_opts(v, rng)
    return ("집합", 3, "도형 해석", f"그림은 전체집합 U의 두 부분집합 A, B를 벤다이어그램으로 나타낸 것이고, 각 영역의 수는 그 영역에 속하는 원소의 개수이다. n(U)={U}일 때, {w}의 값은?", o, ans,
            f"x={U}−({ab}+{b}+{out})={a}. 따라서 {w}={v}.", S.venn(shown))
times(f8, 24)

# F9 도로망 (공사 중 도로)
def f9():
    W, H = rng.randint(3, 5), rng.randint(2, 4)
    edges = []
    for x in range(W + 1):
        for y in range(H + 1):
            if x < W: edges.append(((x, y), (x + 1, y)))
            if y < H: edges.append(((x, y), (x, y + 1)))
    k = rng.choice([1, 2])
    blocked = rng.sample(edges, k)
    via = None
    if rng.random() < 0.4: via = (rng.randint(1, W - 1), rng.randint(1, H - 1))
    def count(s, t, blk):
        from functools import lru_cache
        @lru_cache(None)
        def dp(x, y):
            if (x, y) == t: return 1
            tot = 0
            if x < t[0] and ((x, y), (x + 1, y)) not in blk: tot += dp(x + 1, y)
            if y < t[1] and ((x, y), (x, y + 1)) not in blk: tot += dp(x, y + 1)
            return tot
        return dp(*s)
    bl = set(blocked)
    v = count((0, 0), (W, H), frozenset(bl)) if not via else count((0, 0), via, frozenset(bl)) * count(via, (W, H), frozenset(bl))
    tot = count((0, 0), (W, H), frozenset())
    if v == 0 or v == tot: return None
    o, ans = num_opts(v, rng, lo=1)
    q = f"그림과 같은 도로망에서 × 표시된 도로는 지나갈 수 없다. A 지점에서 B 지점까지 최단 거리로 가는 경우의 수{'' if not via else '를 구할 때, 점 P를 반드시 지나는 경우의 수'}는?"
    return ("경우의 수", 4, "도형 해석", q, o, ans,
            f"각 교차점까지 오는 방법의 수를 왼쪽 아래부터 더해 가면(막힌 도로는 제외) {v}." + ("" if not via else " P까지와 P부터를 따로 세어 곱한다."),
            S.grid_roads(W, H, blocked, [(via, "P")] if via else []))
times(f9, 30)

# F10 영역 색칠 (그림)
def f10():
    kind = rng.choice(["line", "ring", "star"]); n = rng.randint(4, 5) if kind != "line" else rng.randint(4, 6); k = rng.randint(3, 5)
    if kind == "line": edges = [(i, i + 1) for i in range(n - 1)]
    elif kind == "ring": edges = [(i, (i + 1) % n) for i in range(n)]
    else: edges = [(0, i) for i in range(1, n)] + [(i, i % (n - 1) + 1) for i in range(1, n)]
    v = sum(1 for col in itertools.product(range(k), repeat=n) if all(col[a] != col[b] for a, b in edges))
    if v == 0: return None
    o, ans = num_opts(v, rng)
    return ("경우의 수", 4, "도형 해석", f"그림의 {n}개 영역을 서로 다른 {k}가지 색으로 칠하려고 한다. 같은 색을 여러 번 사용해도 되지만 경계선을 공유하는 영역은 서로 다른 색을 칠할 때, 칠하는 방법의 수는?", o, ans,
            f"{'가운데 영역부터' if kind=='star' else '한쪽 끝부터'} 칠하고, {'고리 모양은 마지막 영역이 처음 영역과 같은 색인지로 경우를 나누어' if kind!='line' else '곱의 법칙으로'} 세면 {v}.", S.regions(kind, n))
times(f10, 24)

# F11 대응 그림으로 합성·역함수
def f11():
    X = [1, 2, 3, 4]; perm = rng.sample(X, 4); f = dict(zip(X, perm))
    if all(f[x] == x for x in X): return None
    kind = rng.choice(["ff", "inv", "fff", "cnt"])
    if kind == "ff": a = rng.choice(X); v = f[f[a]]; w = f"(f∘f)({a})"; e = f"f({a})={f[a]}, f({f[a]})={v}"
    elif kind == "inv": a = rng.choice(X); inv = {y: x for x, y in f.items()}; v = inv[a] + f[a]; w = f"f⁻¹({a})+f({a})"; e = f"f⁻¹({a})={inv[a]}, f({a})={f[a]}"
    elif kind == "fff": a = rng.choice(X); v = f[f[f[a]]]; w = f"(f∘f∘f)({a})"; e = f"차례로 대응을 따라가면 {v}"
    else: v = sum(1 for x in X if f[f[x]] == x); w = "(f∘f)(x)=x를 만족시키는 x의 개수"; e = f"각 x에 대해 f(f(x))를 확인하면 {v}개"
    o, ans = num_opts(v, rng, lo=0)
    return ("함수", 3, "도형 해석", f"그림은 집합 X={{1,2,3,4}}에서 X로의 함수 f의 대응을 나타낸 것이다. {w}의 값은?", o, ans, e + ".", S.mapping(X, X, f))
times(f11, 22)

# F12 절댓값 함수 그래프 최솟값
def f12():
    a, b = sorted(rng.sample(range(-4, 6), 2)); c = rng.choice([1, 2])
    f = lambda x: abs(x - a) + c * abs(x - b)
    xs = [x / 10 for x in range(-80, 100)]
    m = min(f(x) for x in xs); mv = min(f(a), f(b))
    pl = S.Plane(-6, 8, -1, max(f(-6), f(8)) * 0.7).axes()
    pl.curve(f, -6, 8).pt((a, f(a)), f"({a}, {f(a)})", -10, -8).pt((b, f(b)), f"({b}, {f(b)})", 4, 14)
    o, ans = num_opts(mv, rng)
    return ("함수", 3, "그래프 해석", f"그림은 함수 y=|x{'−' if a>=0 else '+'}{abs(a)}|+{'' if c==1 else c}|x{'−' if b>=0 else '+'}{abs(b)}|의 그래프이다. 이 함수의 최솟값은?".replace("x−0", "x").replace("x+0", "x"), o, ans,
            f"꺾이는 점 x={a}, x={b}에서의 값 {f(a)}, {f(b)} 중 작은 값 {mv}.", pl.svg())
times(f12, 18)

# F13 이차함수와 직선 위치 관계 (그래프 + 판별식, 접할 때)
def f13():
    p, q = rng.randint(-2, 3), rng.randint(-4, 1); m = rng.choice([-2, -1, 1, 2, 3])
    # y=(x−p)²+q 와 y=mx+k 접할 때 k: (x−p)²+q−mx−k=0, x²−(2p+m)x+p²+q−k=0, D=(2p+m)²−4(p²+q−k)=0 → k = p²+q−(2p+m)²/4
    k = F(p * p + q) - F((2 * p + m) ** 2, 4)
    xt = F(2 * p + m, 2); yt = m * xt + k
    pl = S.Plane(p - 4, p + 4, q - 2, q + 9).axes()
    pl.curve(lambda x: (x - p) ** 2 + q).line((pl.x0, m * pl.x0 + float(k)), (pl.x1, m * pl.x1 + float(k))).pt((float(xt), float(yt)), "T")
    kind = rng.choice(["k", "tx"])
    v = k if kind == "k" else xt + yt
    o, ans = num_opts(v, rng)
    return ("이차함수", 4, "그래프 해석", f"그림과 같이 이차함수 y={P([1,-2*p,p*p+q])}의 그래프와 직선 y={m}x+k가 점 T에서 접한다. {'상수 k의 값' if kind=='k' else '점 T의 x좌표와 y좌표의 합'}은?".replace("1x", "x").replace("−1x", "−x"), o, ans,
            f"x²−({2*p+m})x+{p*p+q}−k=0의 판별식=0 → k={fr(k)}, 접점 x={fr(xt)}, y={fr(yt)}.", pl.svg())
times(f13, 24)

# F14 대칭이동·평행이동 도형 (삼각형)
def f14():
    pts = [(rng.randint(1, 4), rng.randint(1, 4)), (rng.randint(5, 7), rng.randint(1, 3)), (rng.randint(3, 6), rng.randint(4, 6))]
    (ax, ay) = pts[0]
    kind = rng.choice(["yx", "x", "y", "o"])
    tf = {"yx": (lambda x, y: (y, x), "직선 y=x"), "x": (lambda x, y: (x, -y), "x축"), "y": (lambda x, y: (-x, y), "y축"), "o": (lambda x, y: (-x, -y), "원점")}[kind]
    m, n = rng.randint(-3, 3), rng.randint(-3, 3)
    img = [tf[0](x, y) for x, y in pts]; img = [(x + m, y + n) for x, y in img]
    A2 = img[0]; v = A2[0] + A2[1]
    pl = S.Plane(-8, 8, -8, 8).axes()
    pl.poly(pts).pt(pts[0], "A", -12, 12).pt(pts[1], "B").pt(pts[2], "C")
    o, ans = num_opts(v, rng)
    return ("도형의 방정식", 3, "도형 해석", f"그림의 삼각형 ABC를 {tf[1]}에 대하여 대칭이동한 후, x축 방향으로 {m}만큼, y축 방향으로 {n}만큼 평행이동한 삼각형을 A′B′C′이라 하자. 점 A({ax},{ay})의 이동된 점 A′의 x좌표와 y좌표의 합은?", o, ans,
            f"{tf[1]} 대칭: ({tf[0](ax,ay)[0]},{tf[0](ax,ay)[1]}) → 평행이동: ({A2[0]},{A2[1]}) → 합 {v}.", pl.svg())
times(f14, 20)

# ===================== 사례형(실생활) =====================

def c1():  # 가격 인상과 판매량 → 매출 최대
    p0 = rng.choice([2000, 3000, 4000, 5000]); n0 = rng.choice([300, 400, 500, 600]); d = rng.choice([100, 200, 500]); dn = rng.choice([5, 10, 20])
    # 가격 p0+d·t, 판매 n0−dn·t, 매출 R(t)
    R = lambda t: (p0 + d * t) * (n0 - dn * t)
    ts = [F(n0 * d - dn * p0, 2 * d * dn)]
    t = ts[0]
    if t <= 0 or t.denominator != 1: return None
    t = int(t); price = p0 + d * t
    kind = rng.choice(["price", "rev"])
    v = price if kind == "price" else R(t)
    step = d if kind == "price" else max(1000, R(t) // 50 // 1000 * 1000)
    o, ans = num_opts(v, rng, step=step)
    return ("이차함수", 4, "사례형", f"어느 분식점에서 떡볶이 한 접시를 {p0}원에 팔면 하루 {n0}접시가 팔리고, 가격을 {d}원 올릴 때마다 하루 판매량이 {dn}접시씩 줄어든다고 한다. 하루 매출액이 최대가 되도록 할 때, {'한 접시의 가격(원)' if kind=='price' else '하루 최대 매출액(원)'}은?",
            [x for x in o], ans, f"{d}원씩 t번 올리면 매출 R=({p0}+{d}t)({n0}−{dn}t). 꼭짓점 t={t} → 가격 {price}원, 매출 {R(t)}원.")
times(c1, 24)

def c2():  # 울타리 (한 면 벽)
    Lt = rng.choice([40, 60, 80, 100, 120]); walls = rng.choice([1, 0]); parts = rng.choice([1, 2, 3])
    # 벽 1면: 세로 x가 (parts+1)개, 가로 y 1개 (벽 반대편), 총 Lt
    if walls:
        # (parts+1)x + y = Lt, area = x y = x(Lt − (parts+1)x) → x = Lt/(2(parts+1))
        x = F(Lt, 2 * (parts + 1)); y = Lt - (parts + 1) * x; A = x * y
        desc = f"한쪽 면은 담장을 이용하고 나머지 세 면과 칸막이 {parts}개를 길이 {Lt} m의 철망으로 만들어, 직사각형 모양의 닭장을 {parts+1}칸으로 나누려고 한다." if parts > 1 else f"한쪽 면은 담장을 이용하고 나머지 세 면을 길이 {Lt} m의 철망으로 둘러 직사각형 모양의 텃밭을 만들려고 한다."
        if parts == 1: x = F(Lt, 4); y = Lt - 2 * x; A = x * y
    else:
        x = F(Lt, 4); A = x * x; desc = f"길이 {Lt} m의 끈으로 직사각형을 만들려고 한다."
    o, ans = num_opts(A, rng, step=max(1, int(A) // 12))
    return ("이차함수", 3, "사례형", desc + " 만들 수 있는 넓이의 최댓값(m²)은?", o, ans, f"한 변을 x로 두고 넓이를 이차함수로 나타내 꼭짓점에서 최대 → {fr(A)} m².")
times(c2, 14)

def c3():  # 농도 연립
    a, b = rng.choice([(4, 10), (5, 12), (6, 15), (8, 20), (3, 9), (10, 25)]); tot = rng.choice([200, 300, 400, 500, 600])
    target = rng.randint(a + 1, b - 1)
    # x g of a%, (tot−x) of b% → target%
    x = F(tot * (b - target), b - a)
    if x.denominator != 1: return None
    o, ans = num_opts(x, rng, step=10 if x >= 50 else 5, lo=5)
    return ("연립방정식", 3, "사례형", f"{a}%의 소금물과 {b}%의 소금물을 섞어 {target}%의 소금물 {tot} g을 만들려고 한다. 필요한 {a}% 소금물의 양(g)은?", o, ans,
            f"x+y={tot}, {a}x+{b}y={target}×{tot} → x={x}, y={tot-x}.")
times(c3, 16)

def c4():  # 속력
    v1, v2 = rng.choice([(4, 6), (3, 5), (5, 10), (6, 9), (4, 12)]); d = rng.choice([12, 18, 24, 30, 36])
    # 갈 때 v1, 올 때 v2, 총 시간
    T = F(d, v1) + F(d, v2)
    kind = rng.choice(["avg", "time"])
    if kind == "avg": v = F(2 * d, 1) / T; w = "왕복 평균 속력(km/h)"; e = f"총 거리 {2*d} km ÷ 총 시간 {fr(T)} h = {fr(v)} km/h"
    else: v = T; w = "왕복에 걸린 시간(시간)"; e = f"{d}/{v1}+{d}/{v2}={fr(T)}"
    o, ans = num_opts(v, rng)
    return ("연립방정식", 3, "사례형", f"진우는 집에서 {d} km 떨어진 체육관까지 시속 {v1} km로 자전거를 타고 가서, 같은 길을 시속 {v2} km로 돌아왔다. {w}은?".replace("진우는", "준호는"), o, ans, e + ". (평균 속력은 속력의 평균이 아니다.)")
times(c4, 14)

def c5():  # 판매 행렬
    a = [[rng.randint(2, 9) for _ in range(2)] for _ in range(2)]; p = [rng.choice([1000, 1500, 2000, 2500, 3000]) for _ in range(2)]
    tot = [a[i][0] * p[0] + a[i][1] * p[1] for i in range(2)]
    kind = rng.choice(["sum", "diff"])
    v = tot[0] + tot[1] if kind == "sum" else abs(tot[0] - tot[1])
    o, ans = num_opts(v, rng, step=500)
    return ("행렬", 3, "사례형", f"두 매점 P, Q의 하루 판매량을 행렬 A=[[{a[0][0]},{a[0][1]}],[{a[1][0]},{a[1][1]}]] (1행: P, 2행: Q / 1열: 빵, 2열: 우유)로, 빵과 우유의 가격(원)을 행렬 B=[[{p[0]}],[{p[1]}]]로 나타내자. 행렬 AB의 성분을 이용할 때, 두 매점의 매출액의 {'합' if kind=='sum' else '차'}(원)는?",
            o, ans, f"AB=[[{tot[0]}],[{tot[1]}]] (각 매점 매출) → {v}원.")
times(c5, 16)

def c6():  # 시간표/좌석 경우의 수 (brute force)
    subs = ["수학", "영어", "국어", "과학", "사회"][:rng.choice([4, 5])]
    n = len(subs)
    cond = rng.choice(["notfirst", "adj", "notadj", "order"])
    perms = list(itertools.permutations(subs))
    if cond == "notfirst": v = sum(1 for p in perms if p[0] != "수학" and p[-1] != "영어"); d = "수학은 첫째 시간이 아니고 영어는 마지막 시간이 아니도록"
    elif cond == "adj": v = sum(1 for p in perms if abs(p.index("수학") - p.index("과학")) == 1); d = "수학과 과학이 연이어 있도록"
    elif cond == "notadj": v = sum(1 for p in perms if abs(p.index("수학") - p.index("영어")) > 1); d = "수학과 영어가 연이어 있지 않도록"
    else: v = sum(1 for p in perms if p.index("국어") < p.index("수학") < p.index("과학")); d = "국어, 수학, 과학 순서대로 (사이에 다른 과목이 있어도 됨) 배치되도록"
    o, ans = num_opts(v, rng)
    return ("경우의 수", 3, "사례형", f"하루 {n}교시 시간표에 {', '.join(subs)}을(를) 한 시간씩 배정하려고 한다. {d} 시간표를 짜는 경우의 수는?", o, ans, f"조건을 만족하는 배열을 세면 {v}. (여사건·묶음·순서 고정 방법 활용)")
times(c6, 16)

def c7():  # 할인/요금제 비교 → 부등식
    base1, per1 = rng.choice([(10000, 100), (15000, 50), (20000, 40), (5000, 150)]); base2, per2 = rng.choice([(0, 300), (8000, 200), (12000, 120)])
    if per1 == per2: return None
    # base1+per1 x < base2+per2 x 를 만족하는 최소 정수 x (분)
    if per1 > per2: base1, per1, base2, per2 = base2, per2, base1, per1
    # 이제 per1<per2: x > (base1−base2)/(per2−per1)
    th = F(base1 - base2, per2 - per1)
    if th <= 0: return None
    x = math.floor(th) + 1
    o, ans = num_opts(x, rng, step=1 if x < 30 else 5, lo=1)
    return ("부등식", 3, "사례형", f"휴대폰 요금제 A는 기본료 {base1}원에 통화 1분당 {per1}원, 요금제 B는 기본료 {base2}원에 1분당 {per2}원이다. 요금제 A가 B보다 저렴해지려면 한 달 통화 시간이 최소 몇 분이어야 하는가? (분 단위는 자연수)", o, ans,
            f"{base1}+{per1}x<{base2}+{per2}x → x>{fr(th)} → 최소 {x}분.")
times(c7, 14)

# ===== 추가: 다항식·이차/삼차방정식·절대부등식·명제 =====
def rect_fig(a, b, lab_a, lab_b):
    W, H = 260, 170; X0, Y0 = 20, 20; w, h = 220, 130; sx = w * 0.62; sy = h * 0.58
    t = []
    t.append(f'<rect x="{X0}" y="{Y0}" width="{w}" height="{h}" class="bx"/>')
    t.append(f'<line x1="{X0+sx}" y1="{Y0}" x2="{X0+sx}" y2="{Y0+h}" class="bx"/><line x1="{X0}" y1="{Y0+sy}" x2="{X0+w}" y2="{Y0+sy}" class="bx"/>')
    t.append(f'<rect x="{X0}" y="{Y0}" width="{sx}" height="{sy}" class="sh"/>')
    t.append(f'<text x="{X0+sx/2-6}" y="{Y0-5}" class="t">x</text><text x="{X0+sx+(w-sx)/2-6}" y="{Y0-5}" class="t">{lab_a}</text>')
    t.append(f'<text x="{X0+w+4}" y="{Y0+sy/2+4}" class="t">x</text><text x="{X0+w+4}" y="{Y0+sy+(h-sy)/2+4}" class="t">{lab_b}</text>')
    return S.wrap(W + 10, H, "".join(t))
def d1():
    a, b = rng.randint(1, 6), rng.randint(1, 6)
    kind = rng.choice(["coef", "area", "diff"])
    x0 = rng.randint(2, 8)
    if kind == "coef": v = a + b; w = "전체 넓이를 x에 대한 다항식 x²+px+q로 나타낼 때, p의 값"; e = f"(x+{a})(x+{b})=x²+{a+b}x+{a*b} → p={a+b}"
    elif kind == "area": v = (x0 + a) * (x0 + b) - x0 * x0; w = f"x={x0}일 때 색칠하지 않은 부분의 넓이"; e = f"(x+{a})(x+{b})−x²=({a+b})x+{a*b} → x={x0} 대입 {v}"
    else: v = a * b; w = "전체 넓이와 색칠한 정사각형 넓이의 차를 px+q로 나타낼 때, q의 값"; e = f"차=({a+b})x+{a*b} → q={a*b}"
    o, ans = num_opts(v, rng)
    return ("다항식", 3, "도형 해석", f"그림과 같이 가로의 길이가 x+{a}, 세로의 길이가 x+{b}인 직사각형을 한 변의 길이가 x인 정사각형(색칠한 부분)과 나머지 부분으로 나누었다. {w}은?", o, ans, e + ".", rect_fig(a, b, str(a), str(b)))
times(d1, 20)

def d2():  # 직육면체 부피 다항식
    a, b, c = rng.sample(range(1, 7), 3)
    kind = rng.choice(["x2", "x1", "const", "sum"])
    e2, e1, e0 = a + b + c, a * b + b * c + c * a, a * b * c
    v = {"x2": e2, "x1": e1, "const": e0, "sum": 1 + e2 + e1 + e0}[kind]
    w = {"x2": "x²의 계수", "x1": "x의 계수", "const": "상수항", "sum": "모든 계수의 합(상수항 포함)"}[kind]
    o, ans = num_opts(v, rng)
    return ("다항식", 3, "사례형", f"가로, 세로, 높이가 각각 x+{a}, x+{b}, x+{c}인 직육면체 모양의 상자가 있다. 상자의 부피를 x에 대한 다항식으로 나타낼 때, {w}는?", o, ans,
            f"(x+{a})(x+{b})(x+{c})=x³+{e2}x²+{e1}x+{e0} → {v}.")
times(d2, 18)

def d3():  # 정사각형 땅에 길 내기
    side = rng.choice([20, 24, 30, 36, 40]); x = rng.randint(1, 6); kind = rng.choice(["cross", "border"])
    if kind == "cross":
        rem = (side - x) ** 2; d = f"한 변의 길이가 {side} m인 정사각형 모양의 땅에 폭이 x m로 일정한 길을 가로, 세로로 하나씩 수직으로 내었더니 길을 제외한 땅의 넓이가 {rem} m²가 되었다."
        e = f"길을 한쪽으로 모으면 ({side}−x)²={rem} → x={x}"
    else:
        if side - 2 * x <= 0: return None
        rem = (side - 2 * x) ** 2; d = f"한 변의 길이가 {side} m인 정사각형 모양의 땅의 가장자리를 따라 폭 x m로 산책로를 만들었더니 안쪽 땅의 넓이가 {rem} m²가 되었다."
        e = f"({side}−2x)²={rem} → x={x}"
    o, ans = num_opts(x, rng, lo=1)
    return ("이차방정식", 3, "사례형", d + " x의 값은?", o, ans, e + " (0<x 조건으로 다른 근 제외).")
times(d3, 14)

def d4():  # 그래프 교점 = 이차방정식 근
    r1, r2 = sorted(rng.sample(range(-4, 6), 2)); m = rng.randint(-2, 2); n = rng.randint(-3, 3)
    # y=x²+px+q, y=mx+n 교점 x=r1,r2 → x²+(p−m)x+q−n=(x−r1)(x−r2)
    p = m - (r1 + r2); q = n + r1 * r2
    kind = rng.choice(["pq", "dist"])
    if kind == "pq": v = p + q; w = "p+q"; e = f"x²+px+q=mx+n의 두 근이 {r1}, {r2} → p={p}, q={q}"
    else: v = r2 - r1; w = "두 교점의 x좌표의 차"; e = f"근과 계수의 관계: (α−β)²=(α+β)²−4αβ → {v}"
    pl = S.Plane(min(r1, -1) - 2, max(r2, 1) + 2, -6, 12).axes()
    pl.curve(lambda x: x * x + p * x + q).line((pl.x0, m * pl.x0 + n), (pl.x1, m * pl.x1 + n)).pt((r1, m * r1 + n), "A", -12).pt((r2, m * r2 + n), "B")
    o, ans = num_opts(v, rng)
    return ("이차방정식", 4, "그래프 해석", f"그림과 같이 이차함수 y=x²+px+q의 그래프와 직선 y={L(m,n) if m or n else '0'}이 x좌표가 {r1}, {r2}인 두 점 A, B에서 만난다. {w}의 값은?", o, ans, e + ".", pl.svg())
times(d4, 18)

def d5():  # 상자 만들기 (삼차방정식)
    s = rng.choice([12, 14, 16, 18, 20]); x = rng.randint(1, s // 2 - 2)
    V = x * (s - 2 * x) ** 2
    sols = [t for t in range(1, s // 2) if t * (s - 2 * t) ** 2 == V]
    if len(sols) != 1: 
        kind = "small"
    else: kind = "one"
    o, ans = num_opts(min(sols), rng, lo=1)
    return ("삼차방정식", 4, "사례형", f"한 변의 길이가 {s} cm인 정사각형 종이의 네 귀퉁이에서 한 변의 길이가 x cm인 정사각형을 잘라 내고 접어 뚜껑 없는 상자를 만들었더니 부피가 {V} cm³가 되었다. x가 될 수 있는 자연수 중 가장 작은 값은?", o, ans,
            f"x({s}−2x)²={V}을 정리한 삼차방정식에 x=1,2,…를 대입(인수정리)하면 자연수 해 {', '.join(map(str,sols))} → 최솟값 {min(sols)}.")
times(d5, 14)

def d6():  # 절대부등식 사례
    kind = rng.choice(["fence", "area_fixed", "two"])
    if kind == "fence":
        Lt = rng.choice([40, 48, 60, 80, 100]); A = (Lt // 4) * (Lt // 2) // 2 if False else F(Lt * Lt, 8)
        o, ans = num_opts(A, rng, step=max(1, int(A) // 10))
        return ("절대부등식", 3, "사례형", f"벽을 한 변으로 하는 직사각형 모양의 화단을 만들려고 한다. 벽을 제외한 세 변의 길이의 합이 {Lt} m일 때, 화단 넓이의 최댓값(m²)은?", o, ans,
                f"세로 x, 가로 y: 2x+y={Lt}. 산술·기하 평균: 2x·y ≤ ((2x+y)/2)² → xy ≤ {fr(A)}.")
    if kind == "area_fixed":
        A = rng.choice([36, 64, 100, 144, 196, 225]); r = math.isqrt(A)
        v = 4 * r
        o, ans = num_opts(v, rng, step=2)
        return ("절대부등식", 3, "사례형", f"넓이가 {A} m²인 직사각형 모양의 땅의 둘레에 울타리를 치려고 한다. 울타리 길이의 최솟값(m)은?", o, ans, f"둘레 2(x+y) ≥ 4√(xy)=4√{A}={v} (정사각형일 때).")
    a, b = rng.choice([(1, 4), (1, 9), (4, 9), (2, 8), (1, 16)]); k = rng.choice([1, 2, 3])
    # x>0, y>0, x+y=k → a/x + b/y min = (√a+√b)²/k
    v = F((math.isqrt(a) + math.isqrt(b)) ** 2, k)
    o, ans = num_opts(v, rng)
    return ("절대부등식", 4, "모의고사형", f"양수 x, y가 x+y={k}를 만족시킬 때, {a}/x+{b}/y의 최솟값은?".replace(" 1/x", " 1/x"), o, ans,
            f"({a}/x+{b}/y)(x+y) ≥ (√{a}+√{b})² (코시–슈바르츠 또는 전개 후 산술·기하) → 최솟값 {fr(v)}.")
times(d6, 20)

def numline(segs, marks):
    W, H = 300, 80; X = lambda v: 20 + (v + 8) / 18 * 260
    t = [f'<line x1="10" y1="50" x2="{W-10}" y2="50" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)"/>']
    for (lo, hi, lo_c, hi_c, yy, col) in segs:
        t.append(f'<line x1="{X(lo):.1f}" y1="{yy}" x2="{X(hi):.1f}" y2="{yy}" stroke="{col}" stroke-width="3"/>')
        t.append(f'<line x1="{X(lo):.1f}" y1="{yy}" x2="{X(lo):.1f}" y2="50" stroke="{col}" stroke-width="1"/><line x1="{X(hi):.1f}" y1="{yy}" x2="{X(hi):.1f}" y2="50" stroke="{col}" stroke-width="1"/>')
        t.append(f'<circle cx="{X(lo):.1f}" cy="{yy}" r="3.5" {"fill='"+col+"'" if lo_c else "fill='none' stroke='"+col+"'"}/><circle cx="{X(hi):.1f}" cy="{yy}" r="3.5" {"fill='"+col+"'" if hi_c else "fill='none' stroke='"+col+"'"}/>')
    for v, lab in marks: t.append(f'<text x="{X(v)-6:.1f}" y="68" class="t">{lab}</text>')
    return S.wrap(W, H, "".join(t))
def d7():  # 명제 – 수직선 진리집합
    p1, p2 = sorted(rng.sample(range(-6, 9), 2))
    if p2 - p1 < 3: return None
    r = rng.randint(1, (p2 - p1) // 2)
    cnt = (p2 - r) - (p1 + r) + 1
    if cnt <= 0: return None
    fig = numline([(p1, p2, True, True, 30, "#ff6b1a")], [(p1, str(p1)), (p2, str(p2))])
    o, ans = num_opts(cnt, rng, lo=1)
    return ("명제", 4, "도형 해석", f"그림은 조건 p의 진리집합 P를 수직선 위에 나타낸 것이다. 조건 q: |x−a|≤{r}에 대하여 q가 p이기 위한 충분조건이 되도록 하는 정수 a의 개수는?", o, ans,
            f"P=[{p1},{p2}]. Q=[a−{r}, a+{r}]⊆P → {p1+r}≤a≤{p2-r} → {cnt}개.", fig)
times(d7, 20)

if __name__ == "__main__":
    from collections import Counter
    print(len(OUT), Counter(o["unit"] for o in OUT), Counter(o["src"] for o in OUT))
