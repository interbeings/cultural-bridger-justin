import math, random
from fractions import Fraction as F
from common import fr, num_opts, uniq

rng = random.Random(55)
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
def dec(x):
    x=float(x)
    return str(int(x)) if x==int(x) else f'{x:g}'
def U(o, unit): return [x + unit for x in o]

def freefall():
    t = rng.randint(2, 6); h = 5 * t * t; kind = rng.choice(["v", "t", "half"])
    if kind == "v":
        o, a = num_opts(10 * t, rng, step=5, lo=5)
        return ("물체의 운동", 2, "모의고사형", f"지면으로부터 {h} m 높이에서 공을 가만히 놓았다. 공이 지면에 닿기 직전의 속력은? (g=10 m/s², 공기 저항 무시)", U(o, " m/s"), a + " m/s", f"{h}=5t² → t={t} s, v=10t={10*t} m/s.")
    if kind == "t":
        o, a = num_opts(t, rng, lo=1)
        return ("물체의 운동", 2, "교과서 심화", f"지면으로부터 {h} m 높이에서 공을 가만히 놓았다. 공이 지면에 닿을 때까지 걸리는 시간은? (g=10 m/s²)", U(o, " s"), a + " s", f"h=½gt² → {h}=5t² → t={t} s.")
    # 낙하 마지막 1초 동안 이동 거리
    d = h - 5 * (t - 1) ** 2
    o, a = num_opts(d, rng, step=5, lo=5)
    return ("물체의 운동", 3, "EBS형", f"지면으로부터 {h} m 높이에서 공을 가만히 놓았다. 공이 지면에 닿기 직전 마지막 1초 동안 이동한 거리는? (g=10 m/s²)", U(o, " m"), a + " m",
            f"전체 시간 {t} s. ({t-1}) s까지 이동 거리 5×{(t-1)**2}={5*(t-1)**2} m → 마지막 1초 {h}−{5*(t-1)**2}={d} m.")
times(freefall, 8*MULT, maxtry=8000)

def horiz():
    t = rng.randint(1, 4); h = 5 * t * t; v = rng.choice([5, 10, 15, 20, 25])
    kind = rng.choice(["x", "speed"])
    if kind == "x":
        o, a = num_opts(v * t, rng, step=5, lo=5)
        return ("물체의 운동", 3, "EBS형", f"높이 {h} m인 곳에서 공을 수평 방향으로 {v} m/s의 속력으로 던졌다. 공이 지면에 닿을 때까지 이동한 수평 거리는? (g=10 m/s²)", U(o, " m"), a + " m", f"{h}=5t² → t={t} s. 수평 등속: {v}×{t}={v*t} m.")
    vy = 10 * t; sp2 = v * v + vy * vy; s = math.isqrt(sp2)
    if s * s != sp2: return None
    o, a = num_opts(s, rng, step=5, lo=5)
    return ("물체의 운동", 3, "모의고사형", f"높이 {h} m인 곳에서 공을 수평 방향으로 {v} m/s로 던졌다. 지면에 닿기 직전 공의 속력은? (g=10 m/s²)", U(o, " m/s"), a + " m/s", f"연직 속도 10×{t}={vy} m/s, 수평 {v} m/s → √({v*v}+{vy*vy})={s} m/s.")
times(horiz, 7*MULT, maxtry=8000)

def impulse():
    m = rng.choice([F(1, 2), F(1), F(2), F(1, 5)]); v1 = rng.choice([10, 20, 30]); v2 = rng.choice([0, 5, 10, 20]); dt = rng.choice([F(1, 10), F(1, 20), F(1, 50), F(1, 100)])
    kind = rng.choice(["bounce", "stop"])
    if kind == "stop": v2 = 0
    dp = m * (v1 + v2); Fv = dp / dt
    if Fv.denominator != 1: return None
    o, a = num_opts(Fv, rng, step=max(1, int(Fv) // 5))
    s = "반대 방향으로 " + str(v2) + " m/s로 튀어나왔다" if v2 else "정지하였다"
    return ("운동량과 충격량", 3, "수능형", f"질량 {fr(m)} kg인 공이 {v1} m/s로 벽에 수직으로 충돌한 후 {s}. 충돌 시간이 {dec(dt)}초일 때, 벽이 공에 작용한 평균 힘의 크기는?",
            U(o, " N"), a + " N", f"Δp={fr(m)}×({v1}+{v2})={fr(dp)} kg·m/s. F=Δp/Δt={fr(dp)}÷{dec(dt)}={a} N.")
times(impulse, 8*MULT, maxtry=8000)

def collide():
    m1, m2 = rng.randint(1, 4), rng.randint(1, 4); v1 = rng.choice([2, 3, 4, 6, 8, 10])
    V = F(m1 * v1, m1 + m2); ke0 = F(m1 * v1 * v1, 2); ke1 = F(m1 + m2, 2) * V * V
    loss = ke0 - ke1
    if V.denominator != 1 or loss.denominator != 1: return None
    kind = rng.choice(["v", "loss"])
    if kind == "v":
        o, a = num_opts(V, rng)
        return ("운동량과 충격량", 2, "모의고사형", f"마찰 없는 수평면에서 질량 {m1} kg, 속력 {v1} m/s인 물체 A가 정지한 질량 {m2} kg인 물체 B와 충돌하여 한 덩어리로 움직였다. 충돌 후 속력은?",
                U(o, " m/s"), a + " m/s", f"운동량 보존: {m1*v1}=({m1}+{m2})v → v={a} m/s.")
    o, a = num_opts(loss, rng)
    return ("운동량과 충격량", 3, "수능형", f"마찰 없는 수평면에서 질량 {m1} kg, 속력 {v1} m/s인 물체 A가 정지한 질량 {m2} kg인 물체 B와 충돌하여 한 덩어리로 움직였다. 충돌 과정에서 감소한 운동 에너지는?",
            U(o, " J"), a + " J", f"v={fr(V)} m/s. 처음 {fr(ke0)} J, 나중 {fr(ke1)} J → 감소 {a} J.")
times(collide, 8*MULT, maxtry=8000)

def neutral():
    c1 = rng.choice([F(1, 10), F(1, 5), F(1, 2), F(1)]); v1 = rng.choice([10, 20, 30, 40]); c2 = rng.choice([F(1, 10), F(1, 5), F(1, 2), F(1)])
    V = c1 * v1 / c2
    if V.denominator != 1 or V > 200: return None
    o, a = num_opts(V, rng, step=max(5, int(V) // 4), lo=5)
    return ("산과 염기", 2, "EBS형", f"{dec(c1)} M HCl 수용액 {v1} mL를 완전히 중화하는 데 필요한 {dec(c2)} M NaOH 수용액의 부피는?", U(o, " mL"), a + " mL",
            f"H⁺ 몰수 {dec(c1)}×{v1}={dec(c1*v1)} mmol = OH⁻ 몰수 {dec(c2)}×V → V={a} mL.")
times(neutral, 7*MULT, maxtry=8000)

def mixion():
    c = F(1, 10); va, vb = rng.choice([(10, 20), (20, 30), (30, 10), (20, 10), (10, 30), (30, 20)])
    h, oh = va * c, vb * c
    na, cl = oh, h
    rem_h, rem_oh = max(h - oh, 0), max(oh - h, 0)
    ions = {"Na⁺": na, "Cl⁻": cl, "H⁺": rem_h, "OH⁻": rem_oh}
    big = max(ions, key=lambda k: ions[k])
    nat = "산성" if rem_h else "염기성"
    water = min(h, oh)
    choices = [f"가장 많이 존재하는 이온은 {big}이다.", f"혼합 용액은 {'염기성' if nat=='산성' else '산성'}이다.",
               f"생성된 물은 {dec(max(h,oh))} mmol이다.", f"Na⁺ 수와 Cl⁻ 수가 같다.",
               f"{'OH⁻' if nat=='산성' else 'H⁺'}이 {dec(abs(h-oh))} mmol 남아 있다."]
    ans = choices[0]; rng.shuffle(choices)
    return ("산과 염기", 3, "수능형", f"0.1 M HCl 수용액 {va} mL에 0.1 M NaOH 수용액 {vb} mL를 섞었다. 혼합 용액에 대한 설명으로 옳은 것은?", choices, ans,
            f"H⁺ {dec(h)} mmol, OH⁻ {dec(oh)} mmol → 물 {dec(water)} mmol 생성, {nat}. 이온 수: Na⁺ {dec(na)}, Cl⁻ {dec(cl)}, " + ("H⁺ " + str(dec(rem_h)) if rem_h else "OH⁻ " + str(dec(rem_oh))) + f" → 가장 많은 것은 {big}.")
times(mixion, 6*MULT, maxtry=8000)

def halflife():
    T = rng.choice([5, 8, 12, 30, 1600, 5730]); n = rng.randint(2, 5)
    kind = rng.choice(["time", "remain"])
    if kind == "time":
        o, a = num_opts(T * n, rng, step=T, lo=T)
        return ("우주와 원소", 2, "모의고사형", f"반감기가 {T}년인 방사성 동위원소의 양이 처음의 1/{2**n}로 줄어드는 데 걸리는 시간은?", U(o, "년"), a + "년", f"1/{2**n}=(1/2)^{n} → 반감기 {n}번: {T*n}년.")
    m0 = 2 ** n * rng.choice([5, 10, 20, 25])
    o, a = num_opts(F(m0, 2 ** n), rng)
    return ("우주와 원소", 2, "교과서 심화", f"반감기가 {T}일인 방사성 동위원소 {m0} g이 있다. {T*n}일 후 남아 있는 양은?", U(o, " g"), a + " g", f"반감기 {n}번 → {m0}×(1/2)^{n}={a} g.")
times(halflife, 7*MULT, maxtry=8000)

def transformer():
    n1 = rng.choice([100, 200, 500, 1000]); n2 = rng.choice([50, 100, 400, 1000, 2000]); v1 = rng.choice([100, 110, 220, 440])
    if n1 == n2: return None
    v2 = F(v1 * n2, n1)
    kind = rng.choice(["V", "I"])
    if kind == "V":
        o, a = num_opts(v2, rng, step=max(1, int(v2) // 4))
        return ("발전과 에너지", 2, "모의고사형", f"1차 코일 {n1}회, 2차 코일 {n2}회인 이상적인 변압기의 1차 코일에 {v1} V를 걸었다. 2차 코일에 걸리는 전압은?", U(o, " V"), a + " V", f"V₂=V₁×N₂/N₁={v1}×{n2}/{n1}={a} V.")
    i1 = rng.choice([1, 2, 4, 5, 10]); i2 = F(i1 * n1, n2)
    o, a = num_opts(i2, rng)
    return ("발전과 에너지", 3, "EBS형", f"1차 코일 {n1}회, 2차 코일 {n2}회인 이상적인 변압기의 1차 코일에 {i1} A의 전류가 흐른다. 2차 코일에 흐르는 전류는?", U(o, " A"), a + " A", f"전력 보존: V₁I₁=V₂I₂, 전류는 감은 수에 반비례 → {i1}×{n1}/{n2}={a} A.")
times(transformer, 7*MULT, maxtry=8000)

def loss():
    k = rng.choice([2, 3, 4, 5, 10]); kind = rng.choice(["up", "down"])
    if kind == "up":
        ans = f"1/{k*k}배"; o = [f"1/{k*k}배", f"1/{k}배", f"{k}배", f"{k*k}배", "1배"]
        e = f"P=VI 일정 → I는 1/{k}배, 손실 I²R → 1/{k*k}배."; q = f"같은 전력을 송전할 때 송전 전압을 {k}배로 높이면 송전선의 전력 손실은 처음의 몇 배가 되는가? (저항 일정)"
    else:
        ans = f"{k*k}배"; o = [f"1/{k*k}배", f"1/{k}배", f"{k}배", f"{k*k}배", "1배"]
        e = f"I는 {k}배 → 손실 I²R은 {k*k}배."; q = f"같은 전력을 송전할 때 송전 전압을 1/{k}로 낮추면 송전선의 전력 손실은 처음의 몇 배가 되는가? (저항 일정)"
    rng.shuffle(o)
    return ("발전과 에너지", 3, "수능형", q, o, ans, e)
times(loss, 6*MULT, maxtry=8000)

def eco():
    p = rng.choice([1000, 2000, 5000, 10000])
    e1 = rng.choice([8, 10, 12, 15, 20]); e2 = rng.choice([10, 15, 20]);
    c1 = p * e1 // 100; c2 = c1 * e2 // 100
    if c1 * e2 % 100: return None
    o, a = num_opts(e2, rng, lo=1)
    return ("생태계", 2, "모의고사형", f"어떤 생태계에서 생산자의 에너지양은 {p}, 1차 소비자는 {c1}, 2차 소비자는 {c2}(단위: kJ)이다. 2차 소비자의 에너지 효율은?", U(o, "%"), a + "%", f"에너지 효율=현 영양 단계 에너지÷전 단계 에너지×100={c2}/{c1}×100={e2}%.")
times(eco, 6*MULT, maxtry=8000)

def codon():
    n = rng.randint(50, 400); kind = rng.choice(["aa", "base"])
    if kind == "aa":
        o, a = num_opts(n, rng, lo=1)
        return ("생명 시스템", 3, "EBS형", f"어떤 mRNA에서 개시 코돈부터 종결 코돈까지(종결 코돈 포함)의 염기 수가 {3*(n+1)}개일 때, 번역되는 폴리펩타이드의 아미노산 수는?", U(o, "개"), a + "개", f"코돈 {n+1}개 중 종결 코돈은 아미노산을 지정하지 않음 → {n}개.")
    a_pct = rng.choice([15, 20, 22, 28, 30, 35]); g = 50 - a_pct
    o, a = num_opts(g, rng, lo=1)
    return ("생명 시스템", 3, "모의고사형", f"이중 가닥 DNA에서 아데닌(A)이 전체 염기의 {a_pct}%일 때, 구아닌(G)의 비율은?", U(o, "%"), a + "%", f"A=T={a_pct}%, G=C → G=(100−{2*a_pct})/2={g}%.")
times(codon, 7*MULT, maxtry=8000)

def energy():
    m = rng.choice([1, 2, 4, 5]); h = rng.choice([5, 10, 20, 45, 80])
    v = math.isqrt(20 * h)
    if v * v != 20 * h: return None
    kind = rng.choice(["v", "E"])
    if kind == "v":
        o, a = num_opts(v, rng, step=5 if v >= 10 else 1, lo=1)
        return ("물체의 운동", 2, "교과서 심화", f"질량 {m} kg인 물체를 {h} m 높이에서 가만히 놓았다. 역학적 에너지 보존을 이용할 때, 지면에 닿기 직전 속력은? (g=10 m/s²)", U(o, " m/s"), a + " m/s", f"mgh=½mv² → v=√(2gh)=√{20*h}={v} m/s.")
    E = m * 10 * h
    o, a = num_opts(E, rng, step=max(5, E // 5))
    return ("물체의 운동", 2, "교과서 심화", f"질량 {m} kg인 물체가 {h} m 높이에서 자유 낙하하여 지면에 닿기 직전의 운동 에너지는? (g=10 m/s², 공기 저항 무시)", U(o, " J"), a + " J", f"mgh={m}×10×{h}={E} J.")
times(energy, 6*MULT, maxtry=8000)

if __name__ == "__main__":
    from collections import Counter
    print(len(OUT), Counter(o["unit"] for o in OUT))
    for o in OUT[::8]: print(o["q"], o["opts"], o["ans"])
