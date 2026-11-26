import random, bank_chi as B
rng=random.Random(12)
GROUPS=[["珍惜","宝贵","珍贵"],["采取","采用"],["信心","信任"],["经验","教训"],["困难","挑战","压力"],["优势","成就","贡献"],["增加","扩大","促进","延长"],["减少","缩小","节省"],
["影响","效果","意义","价值","印象"],["逐渐","始终","仍然"],["居然","果然","难怪","毕竟"],["恐怕","未必","估计"],["立刻","总算"],["保护","维护","保持"],["承担","承认","承受","忍受"],
["积极","主动"],["严格","严重"],["安静","冷静"],["熟悉","陌生"],["复杂","具体","抽象","简单"],["优秀","宝贵"],["可靠","稳定"],["邀请","答应"],["鼓励","称赞","激发"],["寻找","追求","打听"],
["表达","交流","反映","体现"],["改善","恢复"],["避免","预防","躲"],["观察","调查","分析"],["具备","符合"],["实现","赢得"],["方向","目标"],["谦虚","虚心"],["骄傲","傲慢"],
["沮丧","惭愧","委屈","疲惫"],["坚强","勇敢"],["热情","温柔","大方"],["允许","禁止"],["慷慨","大方"],["固执","顽皮"],["朴素","清淡"],["忽视","浪费"]]
def grp(w): return {x for g in GROUPS if w in g for x in g}
W=B.WORDS;OUT=[]
TONES={'a':'āáǎà','e':'ēéěè','i':'īíǐì','o':'ōóǒò','u':'ūúǔù','ü':'ǖǘǚǜ'}
def tone_variants(py):
    res=set()
    for i,ch in enumerate(py):
        for base,ts in TONES.items():
            if ch in ts:
                for t in ts:
                    if t!=ch: res.add(py[:i]+t+py[i+1:])
    return list(res)
def nsyl(py): return py.count(" ")+1  # unused
lvl=lambda w:4 if w['pos'] in("D",) or len(w['w'])==1 else 3
for w in W:
    ex=grp(w['w'])|{w['w']}
    same=[x for x in W if x['pos']==w['pos'] and x['w'] not in ex and x['m']!=w['m']]
    others=[x for x in W if x['w'] not in ex]
    pool=same if len(same)>=4 else others
    # 1 뜻 고르기
    d=rng.sample(pool,4);o=[w['m']]+[x['m'] for x in d];rng.shuffle(o)
    OUT.append(dict(unit="어휘 의미",lvl=3,src="HSK5형",q=f"다음 단어의 뜻으로 가장 알맞은 것은?\n{w['w']}",passage="",opts=o,ans=w['m'],exp=f"{w['w']}({w['py']}): {w['m']}. 예) {w['s'].replace('＿＿',w['w'])}"))
    # 2 단어 고르기
    d=rng.sample(pool,4);o=[w['w']]+[x['w'] for x in d];rng.shuffle(o)
    OUT.append(dict(unit="어휘 의미",lvl=3,src="HSK5형",q=f"'{w['m']}'에 해당하는 중국어 단어는?",passage="",opts=o,ans=w['w'],exp=f"{w['w']}({w['py']}). 보기 단어: "+", ".join(f"{x['w']}={x['m']}" for x in d)))
    # 3 문맥 속 의미
    sent=w['s'].replace('＿＿',f"【{w['w']}】")
    d=rng.sample(pool,4);o=[w['m']]+[x['m'] for x in d];rng.shuffle(o)
    OUT.append(dict(unit="문맥 어휘",lvl=lvl(w)+0,src="HSK6형" if lvl(w)==4 else "HSK5형",q="【 】 안 단어의 의미로 가장 알맞은 것은?",passage=sent,opts=o,ans=w['m'],exp=f"{w['w']}({w['py']}) = {w['m']}."))
    # 4 병음
    tv=tone_variants(w['py']);rng.shuffle(tv)
    alts=tv[:2]
    sl=[x['py'] for x in W if x['w']!=w['w'] and len(x['w'])==len(w['w']) and x['py'] not in alts]
    alts+=rng.sample(sl,4-len(alts)) if len(sl)>=4-len(alts) else []
    if len(alts)==4 and len(set(alts+[w['py']]))==5:
        o=[w['py']]+alts;rng.shuffle(o)
        OUT.append(dict(unit="병음",lvl=3,src="HSK5형",q=f"다음 단어의 병음으로 바른 것은?\n{w['w']}",passage="",opts=o,ans=w['py'],exp=f"{w['w']} = {w['py']} ({w['m']})."))
C=B.CHENGYU
for cy,m in C:
    d=rng.sample([x for x in C if x[0]!=cy],4)
    o=[m]+[x[1] for x in d];rng.shuffle(o)
    OUT.append(dict(unit="성어",lvl=4,src="HSK6형",q=f"다음 성어의 뜻으로 가장 알맞은 것은?\n{cy}",passage="",opts=o,ans=m,exp=f"{cy}: {m}."))
    d=rng.sample([x for x in C if x[0]!=cy],4)
    o=[cy]+[x[0] for x in d];rng.shuffle(o)
    OUT.append(dict(unit="성어",lvl=4,src="HSK6형",q=f"'{m}'의 뜻을 가진 성어는?",passage="",opts=o,ans=cy,exp=f"{cy}. 보기: "+", ".join(f"{x[0]}={x[1]}" for x in d)))
for o in OUT: assert len(set(o['opts']))==5 and o['ans'] in o['opts'],o
if __name__=="__main__":
    from collections import Counter
    print(len(OUT),Counter(o['unit'] for o in OUT))
    for o in OUT[3:12:2]+OUT[-2:]:print(o['q'],o['passage'],o['opts'],o['ans'])
