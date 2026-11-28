"""영어: 학평 독해(18~45번) 유형 구성으로 재편
 - 모의고사에 없는 유형(단어 뜻, 문장 단위 어휘·어법, SAT)을 학평 유형 문항으로 교체
 - 남는 기존 문항(장문 세트, 순서·삽입, 단일 지문 독해, 지문형 어법·어휘)은 유지하고 단원만 학평 유형별로 재분류
"""
import re, random
from eng_mock_a import A
from eng_mock_b import B
from eng_mock_d import D, LETTERS2, NARR2
from eng_mock_c import LETTERS, NARR, BIOS, NOTICES

CIRC = '①②③④⑤'
UNITS = ['목적·심경·주장', '함축·요지·주제·제목', '도표·내용 일치·실용문', '어법·어휘', '빈칸·요약', '글의 순서·흐름', '장문 세트']
TYPE = {  # 유형 → (단원, 학평 번호 표시)
    '목적': ('목적·심경·주장', '18번 유형'), '심경': ('목적·심경·주장', '19번 유형'), '주장': ('목적·심경·주장', '20번 유형'),
    '함축': ('함축·요지·주제·제목', '21번 유형'), '요지': ('함축·요지·주제·제목', '22번 유형'), '주제': ('함축·요지·주제·제목', '23번 유형'),
    '제목': ('함축·요지·주제·제목', '24번 유형'), '도표': ('도표·내용 일치·실용문', '25번 유형'), '내용 일치': ('도표·내용 일치·실용문', '26번 유형'),
    '실용문': ('도표·내용 일치·실용문', '27·28번 유형'), '어법': ('어법·어휘', '29번 유형'), '어휘': ('어법·어휘', '30번 유형'),
    '빈칸': ('빈칸·요약', '31~34번 유형'), '무관': ('글의 순서·흐름', '35번 유형'), '순서': ('글의 순서·흐름', '36·37번 유형'),
    '삽입': ('글의 순서·흐름', '38·39번 유형'), '요약': ('빈칸·요약', '40번 유형'), '장문': ('장문 세트', '41~45번 유형'),
}
Q = {'제목': '다음 글의 제목으로 가장 적절한 것은?', '주제': '다음 글의 주제로 가장 적절한 것은?', '요지': '다음 글의 요지로 가장 적절한 것은?',
     '주장': '다음 글에서 필자가 주장하는 바로 가장 적절한 것은?'}

GRAM = re.compile(r'\{([^|{}]*)\|([^|{}]*)\|([^{}]*)\}')
VOC = re.compile(r'\[([^|\[\]]*)\|([^\[\]]*)\]')
BLK = re.compile(r'<([^<>]*)>')


def plain(p):
    p = GRAM.sub(lambda m: m.group(1), p)
    p = VOC.sub(lambda m: m.group(1), p)
    return BLK.sub(lambda m: m.group(1), p)


def mk(typ, q, p, opts, ans, x, lvl, sh=1):
    u, s = TYPE[typ]
    return dict(u=u, l=lvl, s=s, q=q, p=p, o=opts, a=opts.index(ans), x=x, sh=sh, _t=typ)


def first_upper(s):
    return s[0].upper() + s[1:]


# ── 밑줄 5곳 고르기: 표시된 1곳(틀린 곳) + 지문에서 자동으로 고른 바른 4곳 ──
G_CAND = re.compile(r"\b(which|that|what|who|whose|where|when|whether|is|are|was|were|has|have|had|does|do|did|been|being|itself|themselves|them|it|its|their|those|to [a-z]+|[a-z]{3,}ing|[a-z]{3,}ed|[a-z]{3,}[a-oq-z]ly)\b")
V_CAND = re.compile(r"\b([a-z]{6,})\b")
STOP = {'speed', 'indeed', 'hundred', 'nothing', 'something', 'everything', 'anything', 'during', 'morning', 'evening', 'spring', 'string', 'ceiling', 'feeling', 'because', 'before', 'during', 'without', 'through', 'between', 'should', 'would', 'could', 'people', 'rather', 'another', 'others', 'itself', 'themselves', 'whether', 'although', 'though', 'around', 'instead', 'something', 'someone', 'everything', 'within', 'therefore', 'however', 'whatever', 'beyond', 'toward', 'towards', 'against', 'across', 'whose', 'which', 'where', 'there', 'their', 'these', 'those', 'almost', 'always', 'perhaps', 'already', 'enough', 'little', 'second', 'twenty', 'thirty', 'thousand', 'thousands', 'million', 'millions', 'hundred', 'hundreds', 'example', 'children', 'student', 'students', 'family', 'only', 'early', 'really', 'usually', 'finally', 'simply', 'actually', 'especially', 'certainly', 'nearly', 'likely', 'surprisingly', 'interestingly'}


def underline(p, kind, wrong_idx, rng):
    marks = list((GRAM if kind == 'g' else VOC).finditer(p))
    target = marks[wrong_idx]
    other = GRAM if kind == 'v' else VOC
    base = plain_except(p, kind)
    # base: 다른 표시 제거, 같은 종류 표시는 남긴 상태 → 다시 찾기
    marks = list((GRAM if kind == 'g' else VOC).finditer(base))
    t = marks[wrong_idx]
    text = base[:t.start()] + '\x00' + base[t.end():]
    text = (GRAM if kind == 'g' else VOC).sub(lambda m: m.group(1), text)
    pos = text.index('\x00')
    cand_re = G_CAND if kind == 'g' else V_CAND
    cands = [m for m in cand_re.finditer(text) if m.group(0).lower() not in STOP and abs(m.start() - pos) > 3]
    # 지문 전체에 고르게 퍼지도록 선택
    rng.shuffle(cands)
    chosen = []
    for m in sorted(cands, key=lambda m: rng.random()):
        if all(abs(m.start() - c.start()) > 40 for c in chosen) and abs(m.start() - pos) > 25:
            chosen.append(m)
        if len(chosen) == 4:
            break
    if len(chosen) < 4:
        return None
    spots = sorted([(pos, None)] + [(m.start(), m) for m in chosen], key=lambda x: x[0])
    k = [i for i, (s, m) in enumerate(spots) if m is None][0]
    out = []
    last = 0
    for i, (s, m) in enumerate(spots):
        if m is None:
            out.append(text[last:s] + CIRC[i] + t.group(2))
            last = s + 1
        else:
            out.append(text[last:s] + CIRC[i] + m.group(0))
            last = m.end()
    out.append(text[last:])
    return ''.join(out), k, t


def plain_except(p, kind):
    if kind == 'g':
        p = VOC.sub(lambda m: m.group(1), p)
    else:
        p = GRAM.sub(lambda m: m.group(1), p)
    return BLK.sub(lambda m: m.group(1), p)


def from_passage(d, rng):
    out = []
    P = plain(d['p'])
    x = d['x']
    for typ, opts in d.get('m', []):
        o = opts[:]
        rng.shuffle(o)
        out.append(mk(typ, Q[typ], P, o, opts[0], f'글의 요지: {x}', 3))
    if 'b' in d:
        m = BLK.search(d['p'])
        ans = m.group(1)
        pb = plain(d['p'][:m.start()] + '\x01' + d['p'][m.end():]).replace('\x01', '_' * 12)
        ds = d['b'][:]
        while len(ds) < 4:
            ds.append(['nothing in particular', 'the opposite of what is expected', 'a simple accident'][len(ds) - 1])
        o = [ans] + ds[:4]
        rng.shuffle(o)
        out.append(mk('빈칸', '다음 빈칸에 들어갈 말로 가장 적절한 것은?', pb, o, ans, f'{x} → 빈칸: {ans}', 4))
    if 'i' in d:
        ph, opts = d['i']
        o = opts[:]
        rng.shuffle(o)
        jo = '가' if ph[-1].lower() in 'aeiouyrw' else '이'
        out.append(mk('함축', f"밑줄 친 '{ph}'{jo} 다음 글에서 의미하는 바로 가장 적절한 것은?", P.replace(ph, f'【{ph}】', 1), o, opts[0], f'{x} → \'{ph}\'은(는) "{opts[0]}"라는 뜻이다.', 4))
    if 's' in d:
        sent, pairs = d['s']
        o = [f'{a} — {b}' for a, b in pairs]
        ans = o[0]
        o2 = o[:]
        rng.shuffle(o2)
        out.append(mk('요약', '다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?\n[요약] ' + sent, P, o2, ans, f'{x} → (A) {pairs[0][0]}, (B) {pairs[0][1]}', 4))
    if 'r' in d:
        sents = re.split(r'(?<=[.!?])\s+(?=[A-Z])', P)
        if len(sents) >= 5:
            n = len(sents)
            j = rng.randint(max(2, n - 3), n - 1)  # 삽입 위치(문장 인덱스)
            ss = sents[:j] + [d['r']] + sents[j:]
            st = len(ss) - 5
            if st >= 1 and st <= j:
                txt = ' '.join(ss[:st]) + ' ' + ' '.join(f'{CIRC[i]} {s}' for i, s in enumerate(ss[st:]))
                k = j - st
                out.append(mk('무관', '다음 글에서 전체 흐름과 관계 없는 문장은?', txt, list(CIRC), CIRC[k], f'{x} → {CIRC[k]}은(는) 글의 흐름과 무관한 내용이다.', 3, 0))
    for kind in ('g', 'v'):
        n = len((GRAM if kind == 'g' else VOC).findall(d['p']))
        for w in range(n):
            r = underline(d['p'], kind, w, rng)
            if not r:
                continue
            txt, k, t = r
            if kind == 'g':
                out.append(mk('어법', '다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?', txt, list(CIRC), CIRC[k], f'{CIRC[k]} {t.group(2)} → {t.group(1)} ({t.group(3)})', 3 if w % 2 == 0 else 4, 0))
            else:
                out.append(mk('어휘', '다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 않은 것은?', txt, list(CIRC), CIRC[k], f'{x} → {CIRC[k]} {t.group(2)}은(는) 문맥에 맞지 않고 {t.group(1)}(이)가 적절하다.', 4, 0))
    return out


def letters(rng):
    out = []
    for txt, opts in LETTERS + LETTERS2:
        o = opts[:]
        rng.shuffle(o)
        out.append(mk('목적', '다음 글의 목적으로 가장 적절한 것은?', txt, o, opts[0], f'편지의 핵심 내용: {opts[0]}', 3))
    return out


def narrs(rng):
    out = []
    for txt, ans, ds, who in NARR + NARR2:
        o = [ans] + ds
        rng.shuffle(o)
        q = f"다음 글에 드러난 {who}의 심경 변화로 가장 적절한 것은?" if '→' in ans else f"다음 글에 나타난 {who}의 심경으로 가장 적절한 것은?"
        out.append(mk('심경', q, txt, o, ans, f'상황의 흐름을 따라가면 {who}의 심경은 {ans}이다.', 3))
    return out


def bios(rng):
    out = []
    for txt, who, T, F in BIOS:
        for f in F:
            ts = rng.sample(T, 4)
            o = ts + [f]
            rng.shuffle(o)
            out.append(mk('내용 일치', f'{who}에 관한 다음 글의 내용과 일치하지 않는 것은?', txt, o, f, f"'{f}'는 글의 내용과 다르다.", 3))
    return out


def notices(rng):
    out = []
    for txt, who, T, F in NOTICES:
        for f in rng.sample(F, 2):
            o = rng.sample(T, 4) + [f]
            rng.shuffle(o)
            out.append(mk('실용문', f'{who}에 관한 다음 안내문의 내용과 일치하지 않는 것은?', txt, o, f, f"안내문 내용과 다른 것: '{f}'", 2))
        for t in rng.sample(T, 2):
            o = F[:4] + [t]
            rng.shuffle(o)
            out.append(mk('실용문', f'{who}에 관한 다음 안내문의 내용과 일치하는 것은?', txt, o, t, f"안내문 내용과 일치하는 것: '{t}'", 2))
    return out


# ── 25번 도표: 가상 설문 자료로 그래프와 진술을 만들고 참·거짓을 계산 ──
THEMES = [
    ('students at Greenville High School', 'their favorite after-school activity', ['sports', 'music', 'reading', 'coding', 'volunteering']),
    ('students at Maple Middle School', 'their main way of getting to school', ['walking', 'bus', 'subway', 'bicycle', 'car']),
    ('teenagers in Riverside', 'the device they use most for studying', ['laptops', 'tablets', 'smartphones', 'desktop computers', 'paper books']),
    ('families in Oakton', 'their preferred type of vacation', ['beach trips', 'city tours', 'camping', 'theme parks', 'staying home']),
    ('high school students in Westbrook', 'their favorite type of movie', ['comedy', 'action', 'animation', 'documentary', 'horror']),
    ('students at Hilltop High School', 'their favorite school subject', ['math', 'English', 'science', 'history', 'art']),
    ('adults in Pine City', 'the snack they eat most often', ['fruit', 'chips', 'cookies', 'nuts', 'yogurt']),
    ('residents of Lakeview', 'their main source of news', ['TV', 'newspapers', 'social media', 'news websites', 'radio']),
    ('members of Sunrise Sports Center', 'their preferred way to exercise', ['running', 'swimming', 'cycling', 'yoga', 'team sports']),
    ('teenagers in Brookfield', 'the type of music they listen to most', ['pop', 'hip-hop', 'rock', 'classical', 'jazz']),
]


def partition(rng, n=5, tot=100):
    while True:
        cuts = sorted(rng.sample(range(4, tot - 3), n - 1))
        v = [b - a for a, b in zip([0] + cuts, cuts + [tot])]
        if min(v) >= 4 and len(set(v)) == n:
            return v


def chart_svg(cats, v1, v2, y1, y2):
    W, H, L, Bm, T = 360, 230, 34, 40, 26
    mx = max(v1 + v2)
    top = (mx // 10 + 1) * 10
    gw = (W - L - 10) / len(cats)
    bw = gw * 0.32
    y = lambda val: T + (H - T - Bm) * (1 - val / top)
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="막대그래프" style="font:11px sans-serif">']
    for g in range(0, top + 1, 10):
        s.append(f'<line x1="{L}" x2="{W - 6}" y1="{y(g):.1f}" y2="{y(g):.1f}" stroke="currentColor" stroke-opacity=".15"/><text x="{L - 4}" y="{y(g) + 4:.1f}" text-anchor="end" fill="currentColor">{g}</text>')
    for i, c in enumerate(cats):
        x0 = L + gw * i + gw * 0.16
        for j, (vv, col) in enumerate(((v1[i], 'currentColor" fill-opacity=".35'), (v2[i], '#3b82f6'))):
            xx = x0 + j * bw
            s.append(f'<rect x="{xx:.1f}" y="{y(vv):.1f}" width="{bw - 1:.1f}" height="{y(0) - y(vv):.1f}" fill="{col}"/><text x="{xx + bw / 2:.1f}" y="{y(vv) - 3:.1f}" text-anchor="middle" fill="currentColor">{vv}</text>')
        ws = c.split(' ')
        lines = [c] if len(ws) == 1 else [' '.join(ws[:len(ws) // 2 + len(ws) % 2]), ' '.join(ws[len(ws) // 2 + len(ws) % 2:])]
        for li, ln in enumerate(lines):
            s.append(f'<text x="{L + gw * i + gw / 2:.1f}" y="{H - Bm + 14 + li * 12}" text-anchor="middle" fill="currentColor">{ln}</text>')
    s.append(f'<text x="{L}" y="14" fill="currentColor">(%)</text>')
    s.append(f'<rect x="{W - 120}" y="5" width="10" height="10" fill="currentColor" fill-opacity=".35"/><text x="{W - 106}" y="14" fill="currentColor">{y1}</text>')
    s.append(f'<rect x="{W - 66}" y="5" width="10" height="10" fill="#3b82f6"/><text x="{W - 52}" y="14" fill="currentColor">{y2}</text>')
    s.append('</svg><p class="small" style="text-align:center;margin:4px 0 0">※ 학습용 가상 자료</p>')
    return ''.join(s)


def charts(rng, per=7):
    out = []
    for who, what, cats in THEMES:
        made = 0
        tries = 0
        while made < per and tries < 400:
            tries += 1
            y1 = rng.choice([2015, 2016, 2018, 2019]); y2 = y1 + rng.choice([5, 6, 7])
            v1 = partition(rng)
            v2 = None
            for _ in range(200):
                d = [rng.randint(-9, 9) for _ in range(4)]
                d.append(-sum(d))
                w = [a + b for a, b in zip(v1, d)]
                if abs(d[4]) <= 12 and min(w) >= 3 and len(set(w)) == 5 and sum(1 for x in d if x != 0) >= 4:
                    v2 = w
                    break
            if not v2:
                continue
            cap = lambda c: first_upper(c) if c[0].islower() else c
            pct = lambda c: f'the percentage of respondents who chose {c}'
            S = []
            i2 = max(range(5), key=lambda i: v2[i])
            for i in range(5):
                c = cats[i]
                S.append((f'In {y2}, the percentage of respondents who chose {c} was the highest among the five options.', i == i2))
                diff = v2[i] - v1[i]
                if diff != 0:
                    S.append((f'{first_upper(pct(c))} {"increased" if diff > 0 else "decreased"} from {y1} to {y2}.', True))
                    S.append((f'{first_upper(pct(c))} {"decreased" if diff > 0 else "increased"} from {y1} to {y2}.', False))
                for j in range(5):
                    if i == j:
                        continue
                    if v1[i] != 2 * v1[j]:
                        S.append((f'In {y1}, {pct(c)} was more than twice that of those who chose {cats[j]}.', v1[i] > 2 * v1[j]))
                    if v2[i] != v2[j] and v1[i] != v1[j]:
                        both = v1[i] > v1[j] and v2[i] > v2[j]
                        S.append((f'In both {y1} and {y2}, {pct(c)} was higher than that of those who chose {cats[j]}.', both))
            dec = [i for i in range(5) if v2[i] < v1[i]]
            if len(dec) == 1:
                S.append((f'{cap(cats[dec[0]])} was the only option whose percentage decreased from {y1} to {y2}.', True))
            gaps = [abs(v2[i] - v1[i]) for i in range(5)]
            g = max(gaps)
            if gaps.count(g) == 1:
                ig = gaps.index(g)
                S.append((f'The gap between {y1} and {y2} was the largest for {cats[ig]}.', True))
                other = rng.choice([i for i in range(5) if i != ig])
                S.append((f'The gap between {y1} and {y2} was the largest for {cats[other]}.', False))
            T = [s for s in S if s[1]]
            F = [s for s in S if not s[1]]
            if len(T) < 4 or not F:
                continue
            ts = rng.sample(T, 4)
            f = rng.choice(F)
            sents = ts + [f]
            rng.shuffle(sents)
            k = sents.index(f)
            intro = f'The above graph shows the results of a survey that asked {who} about {what} in {y1} and {y2}.'
            txt = intro + ' ' + ' '.join(f'{CIRC[i]} {s[0]}' for i, s in enumerate(sents))
            out.append(dict(u=TYPE['도표'][0], l=3, s=TYPE['도표'][1], q='다음 도표의 내용과 일치하지 않는 것은?', p=txt, o=list(CIRC), a=k, sh=0,
                            x=f'{CIRC[k]}이(가) 도표와 다르다. ' + ' / '.join(f'{c}: {a}%→{b}%' for c, a, b in zip(cats, v1, v2)),
                            f=chart_svg(cats, v1, v2, y1, y2), _t='도표'))
            made += 1
    return out


# ── 기존 문항 재분류 ──
def classify_old(it):
    q = it['q']
    if it['u'] == '장문 세트':
        return '장문'
    if '순서로' in q:
        return '순서'
    if '들어가기에' in q:
        return '삽입'
    if '관계 없는' in q:
        return '무관'
    if '요약' in q:
        return '요약'
    if '빈칸' in q:
        return '빈칸'
    if '의미하는 바' in q:
        return '함축'
    for t in ('제목', '주제', '요지'):
        if t in q:
            return t
    if '일치' in q:
        return '내용 일치'
    if '어법상 틀린 것은' in q and it['p']:
        return '어법'
    if ('낱말' in q or '네모' in q) and it['p']:
        return '어휘'
    return None


QUOTA = {'목적': 20, '심경': 20, '주장': 30, '함축': 25, '요지': 30, '주제': 25, '제목': 30, '도표': 45, '내용 일치': 30,
         '실용문': 50, '어법': 55, '어휘': 40, '빈칸': 55, '요약': 25, '무관': 20}


def apply(subj, replace_units, rng):
    items = subj['items']
    keep, n_drop = [], 0
    for it in items:
        t = classify_old(it)
        if t is None:
            n_drop += 1
            continue
        u, s = TYPE[t]
        it['u'] = u
        it['s'] = s
        keep.append(it)
    pool = []
    for d in A + B + D:
        pool += from_passage(d, rng)
    pool += letters(rng) + narrs(rng) + bios(rng) + notices(rng) + charts(rng)
    by = {}
    for it in pool:
        by.setdefault(it['_t'], []).append(it)
    for v in by.values():
        rng.shuffle(v)
    chosen = []
    for t, qn in QUOTA.items():
        chosen += by.get(t, [])[:qn]
    rest = [it for t in by for it in by[t][QUOTA.get(t, 0):]]
    rng.shuffle(rest)
    need = n_drop - len(chosen)
    if need > 0:
        # 부족분은 남은 문항에서 유형이 고르게 섞이도록 보충
        rest.sort(key=lambda it: sum(1 for c in chosen if c['_t'] == it['_t']) + rng.random())
        chosen += rest[:need]
    elif need < 0:
        chosen = chosen[:n_drop]
    cnt = {}
    for it in chosen:
        cnt[it['_t']] = cnt.get(it['_t'], 0) + 1
    print('  영어 교체', n_drop, '→ 새 문항', len(chosen), '(후보', len(pool), ')', cnt)
    for i, it in enumerate(chosen):
        it.pop('_t')
        it['id'] = f'EM{i + 1:03d}'
    allit = keep + chosen
    for it in allit:
        if it['l'] == 4 and '[3점]' not in it['q']:
            lines = it['q'].split('\n')
            lines[0] = lines[0].rstrip() + ' [3점]'
            it['q'] = '\n'.join(lines)
    order = {u: i for i, u in enumerate(UNITS)}
    allit.sort(key=lambda it: (order[it['u']], it.get('g', ''), it.get('gi', 0)))
    subj['items'] = allit
    subj['units'] = UNITS
    return subj


# 빈칸 오답이 3개뿐인 지문에 덧붙일 네 번째 오답 (지문 순서 A+B+D 기준 번호)
EXTRA_BLANK = {
    3: 'force stores to lower their prices', 5: 'a skill that only young players have', 11: 'make children compete with each other',
    12: 'a tradition borrowed from ancient Rome', 16: 'what makes it attractive to designers', 18: 'every mistake is quickly forgiven',
    20: 'use it whenever it calls us', 23: 'be measured only in a laboratory', 24: 'events caused only by humans',
    25: 'keep many windows open at once', 26: 'make all speakers think alike', 27: 'giving orders loudly and clearly',
    28: 'a computer that only stores data', 29: 'a playground for wealthy visitors', 30: 'a modern invention of zookeepers',
    32: 'depends only on local beach clean-ups', 33: 'shoppers always want more variety', 34: 'reasons to buy new pottery',
    35: 'washing our hands less often', 36: 'to memorize its lyrics completely', 37: 'cannot be tested today',
    38: 'its color and design', 39: 'confuses children for life', 40: 'adding more parking lots',
    42: 'affect only a small area of land', 43: 'which company sells it', 44: 'success depends on luck',
    45: 'a museum of forgotten words', 46: 'believe whatever we read first', 47: 'its largest tusk',
    48: 'a resource into a danger', 49: 'the one wrapped most beautifully', 50: 'help cities save electricity on holidays',
}
for _i, _d in enumerate(A + B + D):
    if 'b' in _d and len(_d['b']) < 4:
        _d['b'] = _d['b'] + [EXTRA_BLANK[_i]]
