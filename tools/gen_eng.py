import random, bank_eng as B
rng=random.Random(21)
G=[["immense","vast","enormous","substantial"],["sufficient","adequate"],["ambiguous","obscure","subtle"],["inherent","intrinsic","fundamental"],["decline","diminish","deplete"],
["eliminate","discard","abandon","exclude"],["hinder","inhibit","curb","constrain","suppress","prohibit","undermine"],["reveal","demonstrate","illuminate","evident","explicit","transparent"],
["crucial","fundamental","dominant","predominant","prominent"],["stable","persist","sustain","retain"],["enhance","reinforce","facilitate","accelerate"],["modify","transform"],
["thrive","prevail"],["hostile","skeptical"],["tedious","monotonous"],["trivial","redundant"],["novel","innovative","unprecedented"],["plausible","valid","legitimate","feasible"],
["precise","accurate","explicit"],["initiate","generate","emerge"],["assess","scrutinize","interpret"],["contemplate","anticipate"],["fragile","vulnerable"],["identical","distinct"],
["exaggerate","deceptive","manipulate","exploit"],["tolerate","persist"],["intervene","mediate","reconcile"],["profound","intense","radical"],["preliminary","tentative"],["scarce","deplete"],
["diverse","widespread"],["impose","provoke"],["compensate","remedy","alleviate"],["neglect","abandon"],["coincide","simultaneous"],["conceal","suppress"]]
def ex(w): return {x for g in G if w in g for x in g}|{w}
W=B.WORDS;OUT=[]
for w in W:
    pool=[x for x in W if x['w'] not in ex(w['w']) and x['syn']!=w['syn']]
    d=rng.sample(pool,4);o=[w['m']]+[x['m'] for x in d];rng.shuffle(o)
    OUT.append(dict(unit="어휘",lvl=3,src="수능 어휘",q=f"다음 단어의 뜻으로 가장 적절한 것은?\n{w['w']}",passage="",opts=o,ans=w['m'],exp=f"{w['w']}: {w['m']} (≈ {w['syn']}). 예) {w['s']}"))
    d=rng.sample(pool,4);o=[w['syn']]+[x['syn'] for x in d]
    if len(set(o))<5: continue
    rng.shuffle(o)
    OUT.append(dict(unit="어휘",lvl=3,src="SAT 어휘",q=f"Which word is closest in meaning to '{w['w']}'?",passage="",opts=o,ans=w['syn'],exp=f"{w['w']} ≈ {w['syn']} ({w['m']}). 다른 선지: "+", ".join(f"{x['syn']}" for x in d)))
    d=rng.sample(pool,4);o=[w['m']]+[x['m'] for x in d];rng.shuffle(o)
    import re
    sent=re.sub(r'\b('+re.escape(w['w'][:-1])+r'\w*)',r'【\1】',w['s'],count=1)
    if '【' not in sent: sent=w['s']+f"  (【{w['w']}】)"
    OUT.append(dict(unit="문맥 어휘",lvl=4,src="수능 어휘",q="【 】 안 단어의 문맥상 의미로 가장 적절한 것은?",passage=sent,opts=o,ans=w['m'],exp=f"{w['w']} = {w['m']}."))
for o in OUT: assert len(set(o['opts']))==5 and o['ans'] in o['opts']
if __name__=="__main__":
    print(len(OUT));print([o['passage'] for o in OUT if o['passage']][:8])
