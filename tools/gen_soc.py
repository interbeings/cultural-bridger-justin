import random
from fractions import Fraction as F
from common import fr, num_opts, uniq
rng = random.Random(31)
MULT = 6
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

def comp():
    ax, ay, bx, by = [rng.randint(1, 10) for _ in range(4)]
    oa, ob = F(ax, ay), F(bx, by)  # X재 1단위 기회비용(Y재 단위)
    if oa == ob or (ax < bx) == (ay < by) and False: return None
    xadv = "갑국" if oa < ob else "을국"; yadv = "을국" if xadv == "갑국" else "갑국"
    absx = "갑국" if ax < bx else ("을국" if bx < ax else None)
    if absx is None or ay == by: return None
    absy = "갑국" if ay < by else "을국"
    lo, hi = min(oa, ob), max(oa, ob)
    good = F(lo + hi, 2)
    bad = hi + F(1, 2)
    true = f"{xadv}은 X재 생산에 비교 우위가 있다."
    false = [f"{yadv}은 X재 생산에 비교 우위가 있다.",
             f"갑국의 X재 1단위 생산의 기회비용은 Y재 {fr(1/oa)}단위이다." if 1/oa != oa else f"을국의 X재 1단위 생산의 기회비용은 Y재 {fr(1/ob)}단위이다.",
             f"교역 조건이 X재 1단위=Y재 {fr(bad)}단위이면 두 나라 모두 이익을 얻는다.",
             f"{xadv}은 Y재 생산에 비교 우위가 있다."]
    if absx == absy: false.append(f"{'을국' if absx=='갑국' else '갑국'}은 두 재화 모두에 절대 우위가 있다.")
    else: false.append(f"{absx}은 두 재화 모두에 절대 우위가 있다.")
    o = [true] + rng.sample(false, 4); rng.shuffle(o)
    if not uniq(o): return None
    return ("시장경제", 3, "수능형",
            f"갑국과 을국은 X재와 Y재만 생산한다. 1단위 생산에 필요한 노동 시간이 갑국은 X재 {ax}시간·Y재 {ay}시간, 을국은 X재 {bx}시간·Y재 {by}시간이다. 옳은 것은? (비교 우위에 따라 특화·교역)",
            o, true, f"X재 1단위의 기회비용: 갑국 Y재 {fr(oa)}단위, 을국 Y재 {fr(ob)}단위 → {xadv}이 X재, {yadv}이 Y재에 비교 우위. 교역 조건은 X재 1단위=Y재 {fr(lo)}~{fr(hi)}단위 사이여야 둘 다 이익.")
times(comp, 10*MULT, maxtry=8000)

def dep():
    y = rng.choice([10, 12, 14, 15, 16, 18, 20, 25, 30]); o_ = rng.choice([8, 10, 12, 15, 18, 20, 25])
    w = 100 - y - o_
    kind = rng.choice(["total", "old", "index"])
    if kind == "total": v = F(y + o_, w) * 100; name = "총부양비"; e = f"({y}+{o_})/{w}×100"
    elif kind == "old": v = F(o_, w) * 100; name = "노년 부양비"; e = f"{o_}/{w}×100"
    else: v = F(o_, y) * 100; name = "노령화 지수"; e = f"{o_}/{y}×100"
    if v.denominator != 1: return None
    o, a = num_opts(v, rng, step=5 if v > 20 else 2, lo=1)
    return ("미래와 지속가능성", 3, "모의고사형", f"어떤 국가의 인구 구성이 유소년층 {y}%, 생산 가능 인구 {w}%, 노년층 {o_}%일 때, {name}는?", o, a, f"{name}={e}={a}.")
times(dep, 8*MULT, maxtry=8000)

def opp():
    acts = rng.sample([("수학 학원", "편익"), ("농구 시합", "편익"), ("아르바이트", "편익"), ("영화 관람", "편익"), ("독서", "편익")], 3)
    vals = rng.sample(range(20, 90, 5), 3)
    pick = rng.randrange(3)
    others = [vals[i] for i in range(3) if i != pick]
    v = max(others)
    desc = ", ".join(f"{acts[i][0]}(편익 {vals[i]})" for i in range(3))
    o, a = num_opts(v, rng, step=5, lo=5)
    return ("시장경제", 2, "EBS형", f"주말 3시간 동안 {desc} 중 하나만 할 수 있다. {acts[pick][0]}{"를" if acts[pick][0] in ("아르바이트","독서") else "을"} 선택할 때의 기회비용은? (모든 비용은 시간만 고려)", o, a,
            f"기회비용은 포기한 대안 중 가장 큰 가치 → max({', '.join(map(str, others))})={v}.")
times(opp, 6*MULT, maxtry=8000)
