"""통합과학 학평형 자료 해석 문항 생성기 (표 제시 + <보기>, 정답은 코드로 계산)"""
import random
from fractions import Fraction as Fr

COMB = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄱ, ㄴ', 'ㄱ, ㄷ', 'ㄴ, ㄷ', 'ㄱ, ㄴ, ㄷ']


def table(head, rows, cap=None):
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    c = f'<caption>{cap}</caption>' if cap else ''
    return f'<table class="dt">{c}<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


def fmt(x):
    x = Fr(x)
    if x.denominator == 1:
        return str(x.numerator).replace('-', '−')
    v = float(x)
    return (f'{v:.2f}'.rstrip('0').rstrip('.')).replace('-', '−')


def bogi(rng, stmts, head):
    """stmts: [(문장, 참/거짓, 해설)] 중 3개를 골라 <보기> 문항 구성(참 1개 이상)"""
    T = [s for s in stmts if s[1]]
    F = [s for s in stmts if not s[1]]
    for _ in range(50):
        k = rng.choice([1, 2, 2, 3]) if F else 3
        k = min(k, len(T))
        if 3 - k > len(F) or k == 0:
            continue
        pick = rng.sample(T, k) + rng.sample(F, 3 - k)
        rng.shuffle(pick)
        break
    lab = 'ㄱㄴㄷ'
    ans = ', '.join(lab[i] for i, s in enumerate(pick) if s[1])
    i = COMB.index(ans)
    st = rng.choice([s for s in range(3) if s <= i < s + 5])
    q = head + '\n이에 대한 설명으로 옳은 것만을 <보기>에서 있는 대로 고른 것은?\n\x02<보기>\n' + '\n'.join(f'{lab[j]}. {s[0]}' for j, s in enumerate(pick))
    exp = ' '.join(f"{lab[j]}({'○' if s[1] else '×'}): {s[2]}" for j, s in enumerate(pick))
    nt = sum(s[1] for s in pick)
    return q, COMB[st:st + 5], ans, exp, nt


def item(unit, q, opts, ans, exp, fig, lvl):
    q, p = q.split('\n\x02')
    return dict(u=unit, l=lvl, s='자료 해석형', q=q, p=p, o=opts, a=opts.index(ans), x=exp, sh=0, f=fig)


# 1. 물체의 운동 ─ 시간에 따른 속도 표
def g_motion(rng):
    m = rng.choice([1, 2, 3, 4])
    aA = 0
    vA = rng.choice([2, 3, 4, 5, 6])
    aB = rng.choice([1, 2, 3, -1, -2])
    vB0 = rng.choice([0, 2, 4, 6]) if aB > 0 else rng.choice([8, 10, 12])
    ts = [0, 1, 2, 3, 4]
    vb = [vB0 + aB * t for t in ts]
    if min(vb) < 0:
        return None
    fig = table(['시간(s)'] + [str(t) for t in ts], [['A의 속력(m/s)'] + [str(vA)] * 5, ['B의 속력(m/s)'] + [str(v) for v in vb]])
    head = f'표는 직선 위에서 한 방향으로 운동하는 물체 A, B의 속력을 1초 간격으로 나타낸 것이다. B의 질량은 {m} kg이다.'
    dA = vA * 2  # 1~3초
    dB = (vb[1] + vb[3]) / 2 * 2
    S = []
    S.append((f'B의 가속도의 크기는 {abs(aB)} m/s²이다.', True, f'1초마다 속력이 {abs(aB)} m/s씩 변한다.'))
    wa = abs(aB) + rng.choice([1, 2])
    S.append((f'B의 가속도의 크기는 {wa} m/s²이다.', False, f'가속도의 크기는 {abs(aB)} m/s²이다.'))
    S.append((f'B에 작용하는 알짜힘의 크기는 {m * abs(aB)} N이다.', True, f'F=ma={m}×{abs(aB)}={m * abs(aB)} N'))
    S.append((f'B에 작용하는 알짜힘의 방향은 B의 운동 방향과 {"같다" if aB > 0 else "반대이다"}.', True, '속력이 ' + ('증가하므로 같은 방향' if aB > 0 else '감소하므로 반대 방향')))
    S.append((f'B에 작용하는 알짜힘의 방향은 B의 운동 방향과 {"반대이다" if aB > 0 else "같다"}.', False, '속력이 ' + ('증가하므로 알짜힘은 운동 방향과 같다.' if aB > 0 else '감소하므로 알짜힘은 운동 방향과 반대이다.')))
    S.append(('A에 작용하는 알짜힘은 0이다.', True, 'A는 등속 직선 운동을 한다.'))
    cmp = '크다' if dA > dB else ('작다' if dA < dB else None)
    if cmp:
        S.append((f'1초부터 3초까지 이동한 거리는 A가 B보다 {cmp}.', True, f'A: {fmt(dA)} m, B: (속력-시간 그래프 아래 넓이) {fmt(dB)} m'))
        S.append((f'1초부터 3초까지 이동한 거리는 A가 B보다 {"작다" if cmp == "크다" else "크다"}.', False, f'A: {fmt(dA)} m, B: {fmt(dB)} m'))
    d04 = (vb[0] + vb[4]) / 2 * 4
    S.append((f'0초부터 4초까지 B의 이동 거리는 {fmt(d04)} m이다.', True, f'평균 속력 {fmt((vb[0] + vb[4]) / 2)} m/s × 4 s'))
    S.append((f'0초부터 4초까지 B의 이동 거리는 {fmt(d04 + 4)} m이다.', False, f'이동 거리는 {fmt(d04)} m이다.'))
    q, o, a, x, nt = bogi(rng, S, head)
    return item('물체의 운동', q, o, a, x, fig, 4 if nt != 2 else 3)


# 2. 운동량과 충격량 ─ 충돌 전후 표
def g_collision(rng):
    mA = rng.choice([1, 2, 3, 4]); mB = rng.choice([1, 2, 3, 4, 6])
    uA = rng.choice([2, 3, 4, 5, 6, 8]); uB = rng.choice([0, 0, -1, -2, 1])
    vA = rng.choice([-2, -1, 0, 1, 2])
    p = mA * uA + mB * uB
    vB = Fr(p - mA * vA, mB)
    if vB.denominator != 1 or vB <= vA or vB > 12 or uA <= uB:
        return None
    vB = int(vB)
    dt = rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 2)])
    hide = rng.choice(['vB', 'vA'])
    sv = lambda v: fmt(v) if v >= 0 else '(' + fmt(v) + ')'
    rows = [['A', f'{mA}', fmt(uA), fmt(vA) if hide != 'vA' else '㉠'], ['B', f'{mB}', fmt(uB), fmt(vB) if hide != 'vB' else '㉠']]
    fig = table(['물체', '질량(kg)', '충돌 전 속도(m/s)', '충돌 후 속도(m/s)'], rows)
    head = f'표는 마찰이 없는 수평면에서 일직선 위를 운동하던 물체 A, B가 충돌하기 전과 후의 속도를 나타낸 것이다. 오른쪽 방향을 양(+)으로 하며, 충돌 시간은 {fmt(dt)}초이다.'
    hv = vB if hide == 'vB' else vA
    IA = mA * (vA - uA)
    KE0 = Fr(mA * uA * uA + mB * uB * uB, 2); KE1 = Fr(mA * vA * vA + mB * vB * vB, 2)
    S = [(f'㉠은 {fmt(hv)}이다.', True, f'운동량 보존: {mA}×{sv(uA)}+{mB}×{sv(uB)}={mA}×{sv(vA)}+{mB}×{sv(vB)}'),
         (f'㉠은 {fmt(hv + rng.choice([1, 2, -1]))}이다.', False, f'운동량 보존으로 구하면 ㉠={fmt(hv)}이다.'),
         (f'충돌하는 동안 A가 받은 충격량의 크기는 {abs(IA)} N·s이다.', True, f'A의 운동량 변화량 {mA}×({fmt(vA)}−{sv(uA)})={fmt(IA)} kg·m/s'),
         (f'충돌하는 동안 A가 받은 충격량의 크기는 {abs(IA) + mA} N·s이다.', False, f'충격량의 크기는 {abs(IA)} N·s이다.'),
         ('충돌하는 동안 A가 B로부터 받은 충격량의 크기와 B가 A로부터 받은 충격량의 크기는 같다.', True, '작용 반작용으로 두 물체가 받는 충격량은 크기가 같고 방향이 반대이다.'),
         (f'충돌하는 동안 B가 A에 작용한 평균 힘의 크기는 {fmt(Fr(abs(IA)) / dt)} N이다.', True, f'평균 힘 = 충격량 ÷ 시간 = {abs(IA)}÷{fmt(dt)}'),
         (f'충돌하는 동안 B가 A에 작용한 평균 힘의 크기는 {fmt(Fr(abs(IA)) * dt)} N이다.', False, f'평균 힘 = {abs(IA)}÷{fmt(dt)} = {fmt(Fr(abs(IA)) / dt)} N'),
         ]
    if KE0 == KE1:
        S.append(('충돌 전후 A, B의 운동 에너지의 합은 같다.', True, f'충돌 전 {fmt(KE0)} J, 충돌 후 {fmt(KE1)} J로 같다(탄성 충돌).'))
    else:
        S.append(('충돌 전후 A, B의 운동 에너지의 합은 같다.', False, f'충돌 전 {fmt(KE0)} J, 충돌 후 {fmt(KE1)} J로 다르다.'))
    q, o, a, x, nt = bogi(rng, S, head)
    return item('운동량과 충격량', q, o, a, x, fig, 4 if hide == 'vA' or nt == 3 else 3)


# 3. 산과 염기 ─ 혼합 용액의 액성과 이온 수
def g_neutral(rng):
    kH = rng.choice([1, 2, 3]); kO = rng.choice([1, 2, 3])
    if kH == kO:
        kO = kH + 1
    VA = rng.choice([10, 20])
    VB = sorted(rng.sample([10, 20, 30, 40], 3))
    H = Fr(kH * VA, 10)
    mix = []
    for vb in VB:
        OH = Fr(kO * vb, 10)
        mix.append((vb, OH))
    names = ['(가)', '(나)', '(다)']
    fig = table(['혼합 용액', 'HCl(aq) 부피(mL)', 'NaOH(aq) 부피(mL)'], [[n, str(VA), str(vb)] for n, (vb, _) in zip(names, mix)])
    head = f'표는 HCl(aq)과 NaOH(aq)을 서로 다른 부피로 혼합한 용액 (가)~(다)를 나타낸 것이다. HCl(aq) 10 mL에는 H⁺ {kH}N개, NaOH(aq) 10 mL에는 OH⁻ {kO}N개가 들어 있다.'
    def nature(OH):
        return '산성' if H > OH else ('염기성' if H < OH else '중성')
    btb = {'산성': '노란색', '염기성': '파란색', '중성': '초록색'}
    S = []
    for n, (vb, OH) in zip(names, mix):
        nat = nature(OH)
        why = f'H⁺ {fmt(H)}N개, OH⁻ {fmt(OH)}N개 → {nat}'
        S.append((f'{n}는 {nat}이다.', True, why))
        other = rng.choice([x for x in ['산성', '염기성', '중성'] if x != nat])
        S.append((f'{n}는 {other}이다.', False, why))
        S.append((f'{n}에 BTB 용액을 떨어뜨리면 {btb[nat]}을 띤다.', True, f'{nat} 용액에서 BTB는 {btb[nat]}'))
    w = [min(H, OH) for _, OH in mix]
    if w[2] > w[1]:
        S.append(('생성된 물 분자 수는 (다)가 (나)보다 많다.', True, f'물 분자 수 = 반응한 H⁺ 수: (나) {fmt(w[1])}N, (다) {fmt(w[2])}N'))
    else:
        S.append(('생성된 물 분자 수는 (다)가 (나)보다 많다.', False, f'(나)와 (다) 모두 H⁺ {fmt(H)}N개가 모두 반응하여 물 분자 수가 {fmt(w[1])}N개로 같다.' if w[1] == w[2] else f'(나) {fmt(w[1])}N, (다) {fmt(w[2])}N'))
    ions = [H + OH + abs(H - OH) for _, OH in mix]
    # 전체 이온 수 = Cl⁻(H) + Na⁺(OH) + 남은 이온 |H−OH|
    S.append((f'(가)에 들어 있는 전체 이온 수는 {fmt(ions[0])}N개이다.', True, f'Cl⁻ {fmt(H)}N + Na⁺ {fmt(mix[0][1])}N + 남은 이온 {fmt(abs(H - mix[0][1]))}N'))
    S.append((f'(가)에 들어 있는 전체 이온 수는 {fmt(ions[0] + 1)}N개이다.', False, f'Cl⁻ {fmt(H)}N + Na⁺ {fmt(mix[0][1])}N + 남은 이온 {fmt(abs(H - mix[0][1]))}N = {fmt(ions[0])}N'))
    S.append(('(나)와 (다)에 들어 있는 Cl⁻ 수는 같다.', True, 'Cl⁻은 반응에 참여하지 않으며 HCl(aq) 부피가 같다.'))
    q, o, a, x, nt = bogi(rng, S, head)
    return item('산과 염기', q, o, a, x, fig, 4)


# 4. 화학 결합 ─ 가상 원소의 전자 배치
EL = {3: ('Li', '금속', 1), 6: ('C', '비금속', 4), 7: ('N', '비금속', 5), 8: ('O', '비금속', 6), 9: ('F', '비금속', 7),
      11: ('Na', '금속', 1), 12: ('Mg', '금속', 2), 16: ('S', '비금속', 6), 17: ('Cl', '비금속', 7)}


def shells(z):
    s = []
    for cap in (2, 8, 8):
        s.append(min(cap, z)); z -= s[-1]
        if z <= 0:
            break
    return s


def ion_charge(z):
    v = EL[z][2]
    return v if EL[z][1] == '금속' else v - 8


def g_bond(rng):
    zs = rng.sample([3, 8, 9, 11, 12, 16, 17, 7], 4)
    if not any(EL[z][1] == '금속' for z in zs) or sum(EL[z][1] == '비금속' for z in zs) < 2:
        return None
    L = ['W', 'X', 'Y', 'Z']
    fig = table(['원소', '전자 배치(전자 껍질별 전자 수)'], [[l, ', '.join(map(str, shells(z)))] for l, z in zip(L, zs)])
    head = '표는 2, 3주기 원소 W~Z의 전자 껍질별 전자 수를 나타낸 것이다. W~Z는 임의의 원소 기호이다.'
    S = []
    pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]
    rng.shuffle(pairs)
    for a, b in pairs[:4]:
        ta, tb = EL[zs[a]][1], EL[zs[b]][1]
        if ta != tb:
            kind = '이온 결합'
            m, n = (a, b) if ta == '금속' else (b, a)
            cp, cn = ion_charge(zs[m]), -ion_charge(zs[n])
            from math import gcd
            g = gcd(cp, cn); x, y = cn // g, cp // g
            fml = L[m] + (str(x) if x > 1 else '') + L[n] + (str(y) if y > 1 else '')
            sub = lambda s: s.replace('2', '₂').replace('3', '₃')
            S.append((f'{L[m]}와 {L[n]}는 {sub(fml)}의 화학식으로 표현되는 이온 결합 물질을 형성한다.', True, f'{L[m]}은 {cp}+, {L[n]}은 {cn}− 이온이 되어 {cp}:{cn} 전하를 맞춘다.'))
            wf = L[m] + L[n] + '₂' if fml != L[m] + L[n] + '2' else L[m] + L[n]
            if wf != sub(fml):
                S.append((f'{L[m]}와 {L[n]}는 {wf}의 화학식으로 표현되는 이온 결합 물질을 형성한다.', False, f'{L[m]}은 {cp}+, {L[n]}은 {cn}− 이온이 되므로 화학식은 {sub(fml)}이다.'))
        elif ta == '비금속':
            S.append((f'{L[a]}와 {L[b]}는 공유 결합을 형성할 수 있다.', True, '비금속 원소끼리는 전자쌍을 공유한다.'))
            S.append((f'{L[a]}와 {L[b]}가 결합할 때 전자를 주고받아 이온 결합을 형성한다.', False, '비금속 원소끼리는 공유 결합을 형성한다.'))
    for i, z in enumerate(zs):
        if z in (7, 8, 9, 17):
            sh = {7: 3, 8: 2, 9: 1, 17: 1}[z]
            S.append((f'{L[i]}₂ 분자에서 공유 전자쌍 수는 {sh}이다.', True, f'{L[i]}는 원자가 전자 {EL[z][2]}개로 {sh}쌍을 공유한다.'))
            S.append((f'{L[i]}₂ 분자에서 공유 전자쌍 수는 {sh % 3 + 1}이다.', False, f'공유 전자쌍 수는 {sh}이다.'))
    for i in range(4):
        for j in range(i + 1, 4):
            same_g = EL[zs[i]][2] == EL[zs[j]][2]
            same_p = len(shells(zs[i])) == len(shells(zs[j]))
            S.append((f'{L[i]}와 {L[j]}는 같은 족 원소이다.', same_g, f'원자가 전자 수: {L[i]} {EL[zs[i]][2]}, {L[j]} {EL[zs[j]][2]}'))
            S.append((f'{L[i]}와 {L[j]}는 같은 주기 원소이다.', same_p, f'전자 껍질 수: {L[i]} {len(shells(zs[i]))}, {L[j]} {len(shells(zs[j]))}'))
    for i, z in enumerate(zs):
        c = ion_charge(z)
        ez = z - c
        ng = {2: 'He', 10: 'Ne', 18: 'Ar'}[ez]
        wrong = {'He': 'Ne', 'Ne': 'Ar', 'Ar': 'Ne'}[ng]
        S.append((f'{L[i]}의 안정한 이온은 {ng}과 같은 전자 배치를 갖는다.', True, f'{L[i]}는 전자를 {"잃어" if c > 0 else "얻어"} {abs(c)}{"+" if c > 0 else "−"} 이온이 되며 전자 수가 {ez}개가 된다.'))
        S.append((f'{L[i]}의 안정한 이온은 {wrong}과 같은 전자 배치를 갖는다.', False, f'{L[i]} 이온의 전자 수는 {ez}개로 {ng}과 같은 배치이다.'))
    rng.shuffle(S)
    S = S[:9]
    if not any(s[1] for s in S) or sum(1 for s in S if not s[1]) < 2:
        return None
    q, o, a, x, nt = bogi(rng, S, head)
    return item('화학 결합', q, o, a, x, fig, 4 if nt != 2 else 3)


# 5. 발전과 에너지 ─ 변압기
def g_trans(rng):
    V1 = rng.choice([100, 200, 220, 400])
    P = rng.choice([400, 800, 1200, 2000])
    N1 = rng.choice([100, 200, 400]); k = rng.choice([Fr(1, 2), Fr(2), Fr(4), Fr(1, 4), Fr(5)])
    N2 = int(N1 * k)
    V2 = V1 * k; I1 = Fr(P, V1); I2 = Fr(P) / V2
    if V2.denominator != 1:
        return None
    fig = table(['구분', '1차 코일', '2차 코일'], [['코일의 감은 수', str(N1), str(N2)], ['전압(V)', str(V1), '㉠'], ['전류(A)', fmt(I1), '㉡']])
    head = f'표는 1차 코일에 공급되는 전력이 {P} W인 이상적인 변압기의 1차 코일과 2차 코일에 대한 자료이다.'
    S = [(f'㉠은 {fmt(V2)}이다.', True, f'V₁:V₂=N₁:N₂ → V₂={V1}×{N2}/{N1}'),
         (f'㉠은 {fmt(V1 * N1 / N2 if N2 else 0)}이다.', V1 * Fr(N1, N2) == V2, f'V₂={fmt(V2)} V'),
         (f'㉡은 {fmt(I2)}이다.', True, f'이상적인 변압기에서 전력이 같으므로 I₂={P}/{fmt(V2)}'),
         (f'㉡은 {fmt(I1 * k)}이다.', I1 * k == I2, f'I₂=P/V₂={fmt(I2)} A'),
         (f'2차 코일에서 소비되는 전력은 {P} W이다.', True, '이상적인 변압기는 1차와 2차 코일의 전력이 같다.'),
         (f'2차 코일에서 소비되는 전력은 {fmt(P * k)} W이다.', False, f'전력은 보존되어 {P} W이다.'),
         ('이 변압기는 ' + ('전압을 높이는' if k > 1 else '전압을 낮추는') + ' 데 사용된다.', True, f'N₂/N₁={fmt(k)}'),
         ('1차 코일에 직류 전원을 연결해도 2차 코일에 전압이 지속적으로 유도된다.', False, '변압기는 전자기 유도를 이용하므로 교류에서만 작동한다.'),
         ]
    S = [s for s in S if not (s[0].startswith('㉠은 0'))]
    # 중복 진술 제거
    seen = set(); S2 = []
    for s in S:
        if s[0] in seen:
            continue
        seen.add(s[0]); S2.append(s)
    q, o, a, x, nt = bogi(rng, S2, head)
    return item('발전과 에너지·신소재', q, o, a, x, fig, 3 if nt == 2 else 4)


def g_power_line(rng):
    P = rng.choice([1000, 2000, 4000, 6000]) * 1000
    R = rng.choice([2, 4, 5, 10])
    VA = rng.choice([10000, 20000]); n = rng.choice([2, 4, 5])
    VB = VA * n
    IA = Fr(P, VA); IB = Fr(P, VB)
    LA = IA * IA * R; LB = IB * IB * R
    fig = table(['송전 방식', '송전 전력', '송전 전압', '송전선의 저항'], [['A', f'{P // 1000} kW', f'{VA // 1000} kV', f'{R} Ω'], ['B', f'{P // 1000} kW', f'{VB // 1000} kV', f'{R} Ω']])
    head = '표는 발전소에서 같은 전력을 송전하는 두 방식 A, B를 나타낸 것이다.'
    S = [(f'송전선에 흐르는 전류의 세기는 A가 B의 {n}배이다.', True, f'I=P/V이므로 A {fmt(IA)} A, B {fmt(IB)} A'),
         (f'송전선에 흐르는 전류의 세기는 B가 A의 {n}배이다.', False, 'I=P/V에서 전압이 큰 B의 전류가 더 작다.'),
         (f'송전선에서 손실되는 전력은 A가 B의 {n * n}배이다.', True, f'P손실=I²R → (I_A/I_B)²={n * n}'),
         (f'송전선에서 손실되는 전력은 A가 B의 {n}배이다.', False, f'손실 전력은 전류의 제곱에 비례하므로 {n * n}배이다.'),
         (f'A에서 송전선의 손실 전력은 {fmt(LA / 1000)} kW이다.', True, f'I²R={fmt(IA)}²×{R}={fmt(LA)} W'),
         ('송전 전압을 높이면 송전선에서 손실되는 전력이 줄어든다.', True, '같은 전력을 보낼 때 전압이 높을수록 전류가 작아진다.'),
         ('송전선의 저항을 줄이려면 송전선을 가늘게 만들어야 한다.', False, '저항은 단면적에 반비례하므로 굵게 해야 한다.')]
    q, o, a, x, nt = bogi(rng, S, head)
    return item('발전과 에너지·신소재', q, o, a, x, fig, 3 if nt == 2 else 4)


# 6. 생태계 ─ 영양 단계별 에너지양
def g_pyramid(rng):
    E0 = rng.choice([1000, 2000, 5000, 10000])
    effs = [rng.choice([10, 15, 20]), rng.choice([10, 15, 20]), rng.choice([10, 20, 25])]
    E = [E0]
    for e in effs:
        E.append(E[-1] * e / 100)
    if any(Fr(x).denominator != 1 for x in [Fr(int(E[1] * 100), 100), Fr(int(E[2] * 100), 100)]):
        pass
    names = ['생산자', '1차 소비자', '2차 소비자', '3차 소비자']
    fig = table(['영양 단계', '에너지양(상댓값)'], [[n, fmt(Fr(e).limit_denominator(1000))] for n, e in zip(names, E)])
    head = '표는 어떤 안정된 생태계에서 영양 단계별 에너지양을 나타낸 것이다.'
    ef = lambda i: Fr(E[i]).limit_denominator(1000) / Fr(E[i - 1]).limit_denominator(1000) * 100
    S = [(f'1차 소비자의 에너지 효율은 {fmt(ef(1))}%이다.', True, f'{fmt(E[1])}÷{fmt(E[0])}×100'),
         (f'2차 소비자의 에너지 효율은 {fmt(ef(2))}%이다.', True, f'{fmt(E[2])}÷{fmt(E[1])}×100'),
         (f'2차 소비자의 에너지 효율은 {fmt(ef(2) + 5)}%이다.', False, f'{fmt(E[2])}÷{fmt(E[1])}×100={fmt(ef(2))}%')]
    c = ef(3) > ef(2)
    S.append(('에너지 효율은 3차 소비자가 2차 소비자보다 높다.', c, f'3차 {fmt(ef(3))}%, 2차 {fmt(ef(2))}%'))
    S.append(('상위 영양 단계로 갈수록 전달되는 에너지양은 감소한다.', True, '각 단계에서 호흡으로 에너지가 열로 방출되고 일부만 다음 단계로 전달된다.'))
    S.append(('생산자가 가진 에너지는 모두 1차 소비자에게 전달된다.', False, f'1차 소비자로 전달된 에너지는 {fmt(ef(1))}%뿐이다.'))
    S.append(('2차 소비자의 개체 수가 일시적으로 증가하면 1차 소비자의 개체 수는 일시적으로 감소한다.', True, '먹이 관계에 따라 피식자 수가 감소했다가 다시 회복된다.'))
    q, o, a, x, nt = bogi(rng, S, head)
    return item('생태계와 생물 다양성', q, o, a, x, fig, 3 if nt == 2 else 4)


# 7. 우주와 원소 ─ 원자·이온의 구성 입자 수
def g_particles(rng):
    base = rng.sample([(1, [0, 1, 2]), (3, [3, 4]), (6, [6, 7, 8]), (8, [8, 10]), (11, [12]), (12, [12, 13]), (17, [18, 20]), (2, [2]), (5, [5, 6]), (7, [7, 8])], 3)
    parts = []
    z0, ns = base[0]
    if len(ns) >= 2:
        n1, n2 = rng.sample(ns, 2)
        parts.append((z0, n1, z0)); parts.append((z0, n2, z0))
    else:
        parts.append((z0, ns[0], z0)); z1, n1 = base[2][0], base[2][1][0]; parts.append((z1, n1, z1))
    z, ns2 = base[1]
    ch = rng.choice([1, -1, 2, 0])
    parts.append((z, ns2[0], z - ch))
    rng.shuffle(parts)
    L = ['(가)', '(나)', '(다)']
    fig = table(['입자', '양성자 수', '중성자 수', '전자 수'], [[l, str(p), str(n), str(e)] for l, (p, n, e) in zip(L, parts)])
    head = '표는 원자 또는 이온 (가)~(다)를 구성하는 입자 수를 나타낸 것이다.'
    S = []
    for i in range(3):
        for j in range(i + 1, 3):
            pi, pj = parts[i], parts[j]
            iso = pi[0] == pj[0] and pi[1] != pj[1]
            S.append((f'{L[i]}와 {L[j]}는 동위 원소 관계이다.', iso, '양성자 수가 같고 중성자 수가 다르면 동위 원소이다.' if iso else '양성자 수가 다르거나 중성자 수가 같다.'))
            mi, mj = pi[0] + pi[1], pj[0] + pj[1]
            if mi != mj:
                S.append((f'질량수는 {L[i]}가 {L[j]}보다 크다.', mi > mj, f'질량수=양성자 수+중성자 수: {L[i]} {mi}, {L[j]} {mj}'))
    for i, (p, n, e) in enumerate(parts):
        kind = '양이온' if e < p else ('음이온' if e > p else '원자')
        S.append((f'{L[i]}는 {kind}{"이다" if kind != "원자" else "이다"}.', True, f'양성자 {p}개, 전자 {e}개'))
        wrong = rng.choice([k for k in ['양이온', '음이온', '원자'] if k != kind])
        S.append((f'{L[i]}는 {wrong}이다.', False, f'양성자 {p}개, 전자 {e}개이므로 {kind}이다.'))
    q, o, a, x, nt = bogi(rng, S, head)
    return item('우주와 원소', q, o, a, x, fig, 3)


# 8. 생명 시스템 ─ DNA 염기 조성
def g_dna(rng):
    N = rng.choice([100, 200])
    A = rng.choice([10, 15, 20, 30, 35]) * N // 100
    G = N // 2 - A
    a1 = rng.randint(A // 4, A - A // 4) if A >= 4 else A
    g1 = rng.randint(1, G - 1)
    t1 = A - a1; c1 = G - g1
    rows = [['Ⅰ', str(a1), '㉠', str(g1), '?'], ['Ⅱ', '?', str(a1), '?', str(g1)]]
    fig = table(['가닥', 'A', 'T', 'G', 'C'], rows)
    head = f'이중 가닥 DNA X는 가닥 Ⅰ과 Ⅱ로 구성되며, X를 구성하는 염기의 총 개수는 {N}개, 그중 아데닌(A)은 {A}개이다. 표는 Ⅰ과 Ⅱ의 염기 개수 일부를 나타낸 것이다.'
    S = [(f'㉠은 {t1}이다.', True, f'X의 A={A}=Ⅰ의 A+Ⅱ의 A, Ⅱ의 A=Ⅰ의 T → Ⅰ의 T={A}−{a1}={t1}'),
         (f'㉠은 {t1 + 2}이다.', False, f'Ⅰ의 T={A}−{a1}={t1}'),
         (f'X에서 구아닌(G)의 개수는 {G}개이다.', True, f'A=T, G=C이므로 G=({N}−2×{A})÷2={G}'),
         ('X에서 (A+G)/(T+C)=1이다.', True, '상보적 결합으로 A=T, G=C이다.'),
         (f'Ⅱ에서 시토신(C)의 개수는 {g1}개이다.', True, 'Ⅰ의 G와 Ⅱ의 C는 상보적으로 결합한다.'),
         (f'Ⅰ에서 시토신(C)의 개수는 {c1}개이다.', True, f'Ⅰ의 염기 {N // 2}개 중 A {a1}, T {t1}, G {g1}을 빼면 C={c1}'),
         (f'Ⅰ에서 시토신(C)의 개수는 {c1 + 3}개이다.', False, f'C={N // 2}−{a1}−{t1}−{g1}={c1}')]
    if A != G:
        S.append((f'X에서 구아닌(G)의 개수는 {A}개이다.', False, f'G=({N}−2×{A})÷2={G}'))
    q, o, a, x, nt = bogi(rng, S, head)
    return item('생명 시스템', q, o, a, x, fig, 4)


# 9. 지구 시스템 ─ 기권의 높이에 따른 기온
def g_atmos(rng):
    t0 = rng.choice([15, 18, 20]); t11 = rng.choice([-55, -56, -60])
    t50 = rng.choice([-2, 0, -5]); t80 = rng.choice([-90, -85])
    hs = [0, 11, 50, 80, 100]
    ts = [t0, t11, t50, t80, rng.choice([-20, 0, 20])]
    fig = table(['높이(km)'] + [str(h) for h in hs], [['기온(°C)'] + [fmt(t) for t in ts]])
    lab = rng.sample(['A', 'B', 'C', 'D'], 4)
    head = f'표는 어느 지역의 높이에 따른 기온을 나타낸 것이다. 기권은 기온 분포에 따라 0~11 km 구간 {lab[0]}, 11~50 km 구간 {lab[1]}, 50~80 km 구간 {lab[2]}, 80 km 이상 구간 {lab[3]}로 구분된다.'
    A, B, C, D = lab
    S = [(f'{A}에서는 대류가 일어나고 기상 현상이 나타난다.', True, f'{A}(대류권)는 높이 올라갈수록 기온이 낮아지고 수증기가 있다.'),
         (f'{B}에는 오존층이 존재한다.', True, f'{B}(성층권)는 오존이 자외선을 흡수하여 높이 올라갈수록 기온이 높아진다.'),
         (f'{B}는 대기가 불안정하여 대류가 활발하다.', False, f'{B}(성층권)는 위로 갈수록 기온이 높아 대기가 안정하다.'),
         (f'{C}에서는 대류가 일어나지만 기상 현상은 나타나지 않는다.', True, f'{C}(중간권)는 위로 갈수록 기온이 낮아져 대류가 일어나지만 수증기가 거의 없다.'),
         (f'{C}에서는 높이 올라갈수록 기온이 높아진다.', False, f'50 km에서 {fmt(t50)}°C, 80 km에서 {fmt(t80)}°C로 낮아진다.'),
         (f'{D}에서는 오로라가 나타날 수 있다.', True, f'{D}(열권)는 공기가 매우 희박하고 오로라가 나타난다.'),
         (f'{A}에서 높이 1 km 올라갈 때마다 기온은 평균 약 {fmt(Fr(t0 - t11, 11).limit_denominator(10))}°C씩 낮아진다.', True, f'({fmt(t0)}−({fmt(t11)}))÷11'),
         (f'{D}는 공기의 밀도가 {A}보다 크다.', False, '높이 올라갈수록 공기의 밀도는 작아진다.')]
    q, o, a, x, nt = bogi(rng, S, head)
    return item('지구 시스템', q, o, a, x, fig, 3)


# 10. 산화와 환원 ─ 금속의 반응성 실험
def g_redox(rng):
    order = rng.sample(['A', 'B', 'C'], 3)  # 반응성 큰 순
    r = {m: i for i, m in enumerate(order)}
    mets = ['A', 'B', 'C']
    rows = []
    for m in mets:
        rows.append([f'금속 {m}'] + [('—' if m == n else ('○' if r[m] < r[n] else '×')) for n in mets])
    fig = table(['구분', 'A²⁺ 수용액', 'B²⁺ 수용액', 'C²⁺ 수용액'], rows, '○: 금속 표면에 다른 금속이 석출됨, ×: 변화 없음')
    head = '표는 금속 A~C를 각각 A²⁺, B²⁺, C²⁺이 들어 있는 수용액에 넣었을 때의 결과를 나타낸 것이다.'
    hi, mid, lo = order
    S = [(f'반응성은 {hi}가 {lo}보다 크다.', True, f'{hi}는 {lo}²⁺ 수용액에서 {lo}를 석출시킨다.'),
         (f'반응성은 {lo}가 {mid}보다 크다.', False, f'{mid}가 {lo}²⁺ 수용액에서 {lo}를 석출시키므로 {mid}가 더 크다.'),
         (f'{mid}를 {lo}²⁺ 수용액에 넣으면 {mid}는 산화된다.', True, f'{mid}가 전자를 잃고 {mid}²⁺이 된다.'),
         (f'{mid}를 {lo}²⁺ 수용액에 넣으면 {lo}²⁺은 산화된다.', False, f'{lo}²⁺은 전자를 얻어 {lo}로 환원된다.'),
         (f'{hi}를 {mid}²⁺ 수용액에 넣고 반응시키면 수용액 속 양이온 수는 변하지 않는다.', True, '2가 양이온 1개가 줄고 2가 양이온 1개가 생긴다.'),
         (f'{hi}를 {mid}²⁺ 수용액에 넣고 반응시키면 수용액 속 양이온 수는 증가한다.', False, '전하가 같은 2가 이온끼리 1:1로 바뀌므로 변하지 않는다.'),
         (f'{lo}를 {hi}²⁺ 수용액에 넣으면 {hi}가 석출된다.', False, f'{lo}는 {hi}보다 반응성이 작아 반응하지 않는다.')]
    q, o, a, x, nt = bogi(rng, S, head)
    return item('산화와 환원', q, o, a, x, fig, 3 if nt == 2 else 4)


PLAN = [  # (단원, 교체 개수, 교체 대상, 생성기들)
    ('물체의 운동', 30, 'calc', [g_motion]),
    ('운동량과 충격량', 40, 'calc', [g_collision]),
    ('산과 염기', 30, 'calc', [g_neutral]),
    ('화학 결합', 11, 'right', [g_bond]),
    ('발전과 에너지·신소재', 30, 'calc', [g_trans, g_power_line]),
    ('생태계와 생물 다양성', 20, 'calc', [g_pyramid]),
    ('우주와 원소', 20, 'calc', [g_particles]),
    ('생명 시스템', 20, 'calc', [g_dna]),
    ('지구 시스템', 10, 'right', [g_atmos]),
    ('산화와 환원', 7, 'right', [g_redox]),
]


def kind(it):
    if it['p'] or it.get('f') or '<보기>' in it['q'] or it['o'][0] in COMB:
        return 'other'
    if '옳지 않은' in it['q']:
        return 'wrong'
    if '옳은 것' in it['q']:
        return 'right'
    return 'calc'


def apply(items, replace_units, rng):
    drop = set()
    new = []
    for unit, n, kd, gens in PLAN:
        cand = [it['id'] for it in items if it['u'] == unit and kind(it) == kd]
        rng.shuffle(cand)
        assert len(cand) >= n, (unit, kd, len(cand), n)
        drop.update(cand[:n])
        made = []; seen = set(); tries = 0
        while len(made) < n and tries < 5000:
            tries += 1
            g = rng.choice(gens)
            it = g(rng)
            if not it:
                continue
            key = it['q'] + it['p'] + it['f']
            if key in seen:
                continue
            seen.add(key); made.append(it)
        assert len(made) == n, (unit, len(made))
        new += made
    keep = [it for it in items if it['id'] not in drop]
    for i, it in enumerate(new):
        it['id'] = f'SD{i + 1:03d}'
    print(f'  과학 자료 해석형 {len(new)}문항으로 교체')
    return keep + new
