import random, itertools
import stmt_engine as se, bank_soc
src=lambda l:"수능형" if l==4 else "모의고사형"
OUT=[]
bank={k:v for k,v in bank_soc.SOC.items() if k!="한국사"}
OUT+=se.make(bank,54,2,src)
OUT+=se.make({"한국사":bank_soc.SOC["한국사"]},110,3,src)
rng=random.Random(8);seen=set();n=0
TL=bank_soc.TIMELINE
while n<170:
    ev=rng.sample(TL,4)
    if len({y for _,y in ev})<4: continue
    key=tuple(sorted(e for e,_ in ev))
    if key in seen: continue
    seen.add(key)
    lab="가나다라"
    order=sorted(range(4),key=lambda i:ev[i][1])
    ans="-".join(f"({lab[i]})" for i in order)
    perms=["-".join(f"({lab[i]})" for i in p) for p in itertools.permutations(range(4))]
    wrong=[p for p in perms if p!=ans]
    # 그럴듯한 오답: 인접 두 개만 바꾼 것 우선
    near=[]
    for j in range(3):
        o=order[:];o[j],o[j+1]=o[j+1],o[j];near.append("-".join(f"({lab[i]})" for i in o))
    opts=[ans]+near+[rng.choice([w for w in wrong if w not in near])]
    opts=sorted(opts)
    gap=min(abs(ev[i][1]-ev[j][1]) for i in range(4) for j in range(i+1,4))
    lvl=4 if gap<20 else 3
    q="다음 사건을 일어난 순서대로 바르게 나열한 것은?\n"+"  ".join(f"({lab[i]}) {ev[i][0]}" for i in range(4))
    fy=lambda y:f"기원전 {-y}" if y<0 else str(y)
    exp=" → ".join(f"{ev[i][0]}({fy(ev[i][1])})" for i in order)
    OUT.append(dict(unit="한국사",lvl=lvl,src=src(lvl),q=q,opts=opts,ans=ans,exp=exp));n+=1
if __name__=="__main__":
    from collections import Counter
    print(len(OUT),Counter(o['unit'] for o in OUT))
    print(OUT[-1])
