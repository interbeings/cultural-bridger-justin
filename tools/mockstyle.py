"""고1 3·6·9월 전국연합학력평가(학평) 스타일 변환기

사용법: cd tools && python3 build.py && python3 mockstyle.py
 - build.py가 만든 bank.json(또는 저장소 루트의 bank.json)을 읽어 수학·영어·과학·사회를 학평 형식으로 바꿔 ../bank.json에 씁니다.
 - 과목별 문항 수는 그대로 유지합니다(교체한 문항은 새 id를 받아 예전 학습 기록과 섞이지 않습니다).
학평 형식 요약
 - 수학: 30문항 중 5지선다 21 + 단답형 9(30%), 배점 [2점]/[3점]/[4점]
 - 영어(독해 18~45번): 목적·심경·주장·함축·요지·주제·제목·도표·내용 일치·안내문·어법·어휘·빈칸·무관·순서·삽입·요약·장문
 - 통합과학·통합사회: 25문항, 배점 [1.5점]/[2점]/[2.5점], 자료(표·그림·대화·사료) 제시형 중심
"""
import json, os, re, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
CIRC = '①②③④⑤'
COMB = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄱ, ㄴ', 'ㄱ, ㄷ', 'ㄴ, ㄷ', 'ㄱ, ㄴ, ㄷ']
rng = random.Random(2027)


def has_batchim(ch):
    if '가' <= ch <= '힣':
        return (ord(ch) - 0xAC00) % 28 != 0
    if ch.isdigit():
        return ch in '013678'  # 영, 일, 삼, 육, 칠, 팔
    return None


def last_hangul(s):
    s = re.sub(r'\([^()]*\)$', '', s.rstrip())
    for ch in reversed(s):
        if '가' <= ch <= '힣' or ch.isdigit():
            return ch
        if ch.isalpha():
            return None
    return None


def fix_topic_josa(q):
    """'값는?' → '값은?' 처럼 받침에 맞지 않는 조사 교정"""
    def f(m):
        word, j = m.group(1), m.group(2)
        ch = last_hangul(word)
        if ch is None:
            return m.group(0)
        b = has_batchim(ch)
        return word + ('은' if b else '는') + '?'
    return re.sub(r'(\S+?)([은는])\?', f, q)


def tag_points(q, pts):
    """첫 번째 물음표가 있는 줄 끝에 배점 표시"""
    lines = q.split('\n')
    for i, l in enumerate(lines):
        if re.search(r'[?？]\s*$', l) or l.rstrip().endswith('구하시오.'):
            lines[i] = l.rstrip() + f' [{pts}]'
            return '\n'.join(lines)
    return q.rstrip() + f' [{pts}]'


def to_short_answer(q):
    lines = q.split('\n')
    for i, l in enumerate(lines):
        m = re.search(r'(\S+?)([은는])\?\s*$', l)
        if m:
            word = m.group(1)
            ch = last_hangul(word)
            b = has_batchim(ch) if ch else (m.group(2) == '은')
            lines[i] = l[:m.start()] + word + ('을' if b else '를') + ' 구하시오.'
            return '\n'.join(lines)
    return None


# ───────────────────────── 수학 ─────────────────────────
MATH_PTS = {2: '2점', 3: '3점', 4: '4점'}


def math_style(items):
    for it in items:
        it['q'] = fix_topic_josa(it['q'])
        if it['s'] in ('모의고사형', '교과서 심화', 'EBS형', '수능형'):
            it['s'] = '학평형'
    # 단답형 30%: 정답이 1~999 자연수이고 선지가 모두 정수인 문항에서 단원·난이도 비율을 고려해 선정
    def ok(x):
        a = x['o'][x['a']]
        if not re.fullmatch(r'[1-9]\d{0,2}', a):
            return False
        if not all(re.fullmatch(r'−?\d+', o) for o in x['o']):
            return False
        return to_short_answer(x['q']) is not None
    target = round(len(items) * 0.30)
    el = [x for x in items if ok(x)]
    w = {2: 0.35, 3: 1.0, 4: 1.6}
    el.sort(key=lambda x: rng.random() ** (1 / w[x['l']]), reverse=True)
    chosen = set(id(x) for x in el[:target])
    for it in items:
        if id(it) in chosen:
            it['q'] = to_short_answer(it['q'])
            it['sa'] = 1
            it['sh'] = 0
        it['q'] = tag_points(it['q'], MATH_PTS[it['l']])
    return items


# ─────────────────────── 과학·사회 공통 ───────────────────────
TAM_PTS = {2: '1.5점', 3: '2점', 4: '2.5점'}
SRC_MAP = {'모의고사형': '학평형', 'EBS형': '학평형', '수능형': '학평 고난도', '교과서 심화': '학평형'}


def topic_of(q):
    m = re.match(r'(.+?)(?:에 대한 설명)?으?로 옳(?:은|지 않은) 것', q)
    return m.group(1) if m else None


def dialogue(it, subj):
    """<보기> ㄱ·ㄴ·ㄷ 진술형 → 학생 A·B·C 대화형"""
    head, *st = it['q'].split('\n')
    if len(st) != 3 or not all(re.match(r'[ㄱㄴㄷ]\. ', s) for s in st):
        return False
    tp = topic_of(head)
    if not tp:
        return False
    who = ['A', 'B', 'C']
    say = [f"학생 {w}: {s[3:]}" for w, s in zip(who, st)]
    frame = rng.choice([
        f"다음은 {tp}에 대해 학생 A, B, C가 나눈 대화이다.",
        f"다음은 {tp}에 대한 수업 장면이다.",
        f"다음은 {tp}에 대해 모둠 활동 중 학생 A, B, C가 발표한 내용이다.",
    ])
    tr = dict(zip('ㄱㄴㄷ', who))
    it['q'] = frame + "\n제시한 내용이 옳은 학생만을 있는 대로 고른 것은?"
    it['p'] = ('교사: 오늘 배운 내용을 한 가지씩 말해 볼까요?\n' if '수업' in frame else '') + '\n'.join(say)
    it['o'] = [''.join(tr.get(c, c) for c in o) for o in it['o']]
    it['x'] = re.sub(r'([ㄱㄴㄷ])\(', lambda m: '학생 ' + tr[m.group(1)] + '(', it['x'])
    return True


def note_form(it):
    """'~에 대한 설명으로 옳지 않은 것은?' → 학생 정리 노트의 ①~⑤ 중 옳지 않은 것"""
    tp = topic_of(it['q'])
    if not tp or '옳지 않은' not in it['q'] or it['p']:
        return False
    opts = it['o'][:]
    it['p'] = f"[{tp} 정리 노트]\n" + '\n'.join(f"{CIRC[i]} {o}" for i, o in enumerate(opts))
    it['q'] = f"다음은 학생이 {tp}에 대해 정리한 노트이다. ①~⑤ 중 옳지 않은 것은?"
    it['x'] = f"틀린 내용은 {CIRC[it['a']]}입니다. " + it['x']
    it['o'] = list(CIRC)
    it['sh'] = 0
    return True


def tam_style(items, subj):
    nd = nn = 0
    for it in items:
        it['s'] = SRC_MAP.get(it['s'], it['s'])
        plain_bogi = '<보기>' in it['q'] and not it['p'] and not it.get('f') and it['q'].count('\n') == 3
        if plain_bogi and rng.random() < 0.55 and dialogue(it, subj):
            it['s'] = '대화 자료형'; nd += 1
        elif '옳지 않은' in it['q'] and not it['p'] and rng.random() < 0.5 and note_form(it):
            it['s'] = '정리 노트형'; nn += 1
    print(f'  {subj}: 대화형 {nd}, 정리 노트형 {nn}')
    return items


def finish_tam(items):
    for it in items:
        it['q'] = tag_points(it['q'], TAM_PTS[it['l']])
    return items


# ─────────────────────────── 실행 ───────────────────────────
def replace_units(items, drop, new_items, prefix):
    """drop(it)이 참인 문항을 new_items로 같은 개수만큼 교체(새 id)"""
    keep = [it for it in items if not drop(it)]
    n = len(items) - len(keep)
    assert len(new_items) >= n, (prefix, len(new_items), n)
    rng.shuffle(new_items)
    add = new_items[:n]
    for i, it in enumerate(add):
        it['id'] = f'{prefix}{i + 1:03d}'
    return keep + add


def main():
    root = os.path.join(HERE, '..', 'bank.json')
    src = os.path.join(HERE, 'bank.json') if os.path.exists(os.path.join(HERE, 'bank.json')) else root
    bank = json.load(open(src))
    before = {k: len(v['items']) for k, v in bank.items()}
    import mock_english, mock_science, mock_social
    # 수학
    bank['math']['items'] = math_style(bank['math']['items'])
    # 영어
    bank['english'] = mock_english.apply(bank['english'], replace_units, rng)
    # 과학
    sci = bank['science']
    sci['items'] = mock_science.apply(sci['items'], replace_units, rng)
    sci['items'] = finish_tam(tam_style(sci['items'], '과학'))
    # 사회
    soc = bank['social']
    soc['items'] = mock_social.apply(soc['items'], replace_units, rng)
    soc['items'] = finish_tam(tam_style(soc['items'], '사회'))
    # <보기>·학생 조합·번호형 선지는 순서를 섞지 않고 정해진 순서로 표시
    ABC = ['A', 'B', 'C', 'A, B', 'A, C', 'B, C', 'A, B, C']
    for k in ('math', 'english', 'science', 'social'):
        for it in bank[k]['items']:
            for seq in (COMB, ABC, list(CIRC)):
                if all(o in seq for o in it['o']):
                    ans = it['o'][it['a']]
                    it['o'] = sorted(it['o'], key=seq.index)
                    it['a'] = it['o'].index(ans)
                    it['sh'] = 0
    for k in ('science', 'social'):
        order = bank[k]['units']
        bank[k]['items'].sort(key=lambda it: order.index(it['u']))
    after = {k: len(v['items']) for k, v in bank.items()}
    assert before == after, (before, after)
    for k, v in bank.items():
        ids = [it['id'] for it in v['items']]
        assert len(ids) == len(set(ids)), k
        for it in v['items']:
            assert len(it['o']) == 5 and len(set(it['o'])) == 5 and 0 <= it['a'] < 5, (k, it['id'], it['q'][:40])
            assert it['u'] in v['units'], (k, it['u'])
    json.dump(bank, open(root, 'w'), ensure_ascii=False, separators=(',', ':'))
    for k in ('math', 'english', 'science', 'social'):
        I = bank[k]['items']
        print(k, len(I), Counter(it['u'] for it in I).most_common(), '단답형', sum(1 for it in I if it.get('sa')))


if __name__ == '__main__':
    main()
