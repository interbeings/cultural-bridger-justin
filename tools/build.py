import json,re,sys
sys.path.insert(0,'.')
from collections import Counter
ns={}
for f in ['math','math2','english','chinese','science','social','thinking']:
    exec(open(f+'.py').read(),ns)
import gen_math,gen_think,gen_sci,gen_soc
for f in ['eng2','eng3','eng4','chi2','sci2','soc2','soc3']:
    exec(open(f+'.py').read(),ns)
CIRC='①②③④⑤'
def conv(raw,src_fn,has_passage):
    out=[]
    for r in raw:
        r=list(r)
        if has_passage:
            unit,lvl,q,p,opts,exp=r
        else:
            if r[3]=="K":
                unit,lvl,q,_,ans,exp=r
                out.append(dict(unit=unit,lvl=lvl,src=src_fn(unit,lvl),q=q,passage="",opts=['ㄱ','ㄴ','ㄷ','ㄱ, ㄴ','ㄱ, ㄷ','ㄴ, ㄷ','ㄱ, ㄴ, ㄷ'],ans=ans,exp=exp,K=1));continue
            unit,lvl,q,opts,exp=r;p=""
        ans=opts[0]
        if all(o in CIRC for o in opts): opts=sorted(opts,key=CIRC.index)
        elif all(o.startswith('(') and '-' in o for o in opts): opts=sorted(opts)
        out.append(dict(unit=unit,lvl=lvl,src=src_fn(unit,lvl),q=q,passage=p,opts=opts,ans=ans,exp=exp))
    return out
def esrc(u,l): return "SAT형" if u.startswith("SAT") else ("수능형" if l==4 else "모의고사형")
def csrc(u,l): return "HSK6형" if l==4 else "HSK5형"
def gsrc(u,l): return "수능형" if l==4 else ("모의고사형" if l==3 else "교과서 심화")
import gen_eng,gen_chi,gen_soc2,stmt_engine,bank_sci
from eset1 import SETS1
from eset2 import SETS2
from eset3 import SETS3
from eset4 import SETS4
from eset5 import SETS5
import importlib
SETS=[]
for _i in range(1,40):
    try: _m=importlib.import_module(f"eset{_i}")
    except ModuleNotFoundError: continue
    SETS+=getattr(_m,f"SETS{_i}")
set_items=[]
for gi,st in enumerate(SETS):
    for qi,(typ,q,opts,exp) in enumerate(st['qs']):
        ans=opts[0]
        if all(o in CIRC for o in opts): opts=sorted(opts,key=CIRC.index)
        set_items.append(dict(unit="장문 세트",lvl=st['lvl'],src="수능 장문형",q=f"[{typ}] "+q,passage=st['passage'],opts=opts,ans=ans,exp=exp,g=f"S{gi+1:03d}",gi=qi+1,gn=len(st['qs'])))
sci_stmt=stmt_engine.make(bank_sci.SCI,50,1,lambda l:"수능형" if l==4 else "모의고사형")
import gen_math2,gen_think2,gen_eng2
exec(open('eng5.py').read(),ns);exec(open('chi3.py').read(),ns)
import gen_fig
ns['M']=ns['M']+ns['M2']+gen_math.OUT+gen_math2.OUT+gen_fig.OUT
ns['E']=set_items+ns['E']+conv(ns['E2raw'],esrc,True)+conv(ns['E3raw'],esrc,True)+conv(ns['E4raw'],esrc,True)+gen_eng.OUT+gen_eng2.OUT+conv(ns['E5raw'],esrc,True)
ns['C']=ns['C']+conv(ns['C2raw'],csrc,True)+gen_chi.OUT+conv(ns['C3raw'],csrc,True)
ns['S']=ns['S']+gen_sci.OUT+conv(ns['S2raw'],gsrc,False)+sci_stmt
ns['P']=ns['P']+gen_soc.OUT+conv(ns['P2raw'],gsrc,False)+conv(ns['P3raw'],gsrc,False)+gen_soc2.OUT
ns['T']=ns['T']+gen_think.OUT+gen_think2.OUT
RENAME={'english':{'빈칸 추론':'독해(단일 지문)','요약문':'독해(단일 지문)','함축 의미':'독해(단일 지문)','주제/요지':'독해(단일 지문)','장문 독해':'독해(단일 지문)',
  '순서 배열':'글의 순서·흐름','문장 삽입':'글의 순서·흐름','무관한 문장':'글의 순서·흐름','SAT Words in Context':'SAT','SAT Transitions':'SAT','SAT Logical Inference':'SAT'},
 'chinese':{'어휘 빈칸':'어휘 빈칸·구별','어휘 구별':'어휘 빈칸·구별','문법':'문법·어순','어순':'문법·어순','독해':'독해·번역','번역':'독해·번역'},
 'science':{'물질의 성질':'화학 결합','신소재':'발전과 에너지·신소재','발전과 에너지':'발전과 에너지·신소재','변화와 다양성':'생태계와 생물 다양성','생태계':'생태계와 생물 다양성'},
 'thinking':{'논리 퍼즐':'논리·추론','논리 추론':'논리·추론','창의 추론':'논리·추론','확률 직관':'경우의 수·확률','경우의 수':'경우의 수·확률'}}
subj=[('math','수학','M'),('english','영어','E'),('chinese','중국어','C'),('science','과학','S'),('social','사회','P'),('thinking','사고력','T')]
out={}
import random
rng=random.Random(2026)
COMB=['ㄱ','ㄴ','ㄷ','ㄱ, ㄴ','ㄱ, ㄷ','ㄴ, ㄷ','ㄱ, ㄴ, ㄷ']
def rebalance(o,ans):
    # ㄱㄴㄷ 보기형
    if all(x in COMB for x in o) and ans in COMB:
        i=COMB.index(ans);starts=[st for st in range(3) if st<=i<st+5]
        st=rng.choice(starts);return COMB[st:st+5]
    # 등차 정수 선지
    try: v=[int(x.replace('−','-')) for x in o]
    except ValueError: return o
    d=v[1]-v[0]
    if d<=0 or any(v[k+1]-v[k]!=d for k in range(4)): return o
    a=int(ans.replace('−','-'));pos=rng.randrange(5)
    nv=[a+(k-pos)*d for k in range(5)]
    if min(v)>=0 and min(nv)<0: return o
    return [str(x).replace('-','−') for x in nv]
def isnum(x): return any(ch.isdigit() or ch in '√π' for ch in x) and len(x)<16
for key,name,var in subj:
    items=[];seenq={}
    for i,e in enumerate(ns[var]):
        kq=e['q']+'|'+e.get('passage','')+'|'+'/'.join(sorted(e['opts']))+e.get('fig','')
        if kq in seenq and seenq[kq]==e['ans']: continue
        seenq.setdefault(kq,e['ans'])
        e=dict(e);e['unit']=RENAME.get(key,{}).get(e['unit'],e['unit'])
        o=rebalance(e['opts'],e['ans'])
        o=list(o)
        assert e['ans'] in o and len(o)==5 and len(set(o))==5,(key,i,e['q'][:30])
        is_ord=all(isnum(x) for x in o) or o[0] in('①','ㄱ','ㄱ, ㄴ') or o[0].startswith('(')
        items.append(dict(id=f"{var}{i+1:02d}",u=e['unit'],l=e['lvl'],s=e['src'],q=e['q'],p=e.get('passage',''),o=o,a=o.index(e['ans']),x=e['exp'],sh=0 if is_ord else 1,**({'g':e['g'],'gi':e['gi'],'gn':e['gn']} if 'g' in e else {}),**({'f':e['fig']} if e.get('fig') else {})))
    out[key]=dict(name=name,items=items)
    print(key,len(items),dict(Counter(it['l'] for it in items)),'fixed-pos answers',Counter(it['a'] for it in items if not it['sh']))
MATH_ORDER=[("다항식","공통수학1 · 1학기"),("복소수","공통수학1 · 1학기"),("이차방정식","공통수학1 · 1학기"),("이차함수","공통수학1 · 1학기"),
 ("삼차방정식","공통수학1 · 1학기"),("연립방정식","공통수학1 · 1학기"),("부등식","공통수학1 · 1학기"),("경우의 수","공통수학1 · 1학기"),("행렬","공통수학1 · 1학기"),
 ("도형의 방정식","공통수학2 · 2학기"),("집합","공통수학2 · 2학기"),("명제","공통수학2 · 2학기"),("절대부등식","공통수학2 · 2학기"),
 ("함수","공통수학2 · 2학기"),("유리함수","공통수학2 · 2학기"),("무리함수","공통수학2 · 2학기")]
MB=dict(MATH_ORDER)
for it in out['math']['items']:
    assert it['u'] in MB, it['u']
    it['b']=MB[it['u']]
out['math']['units']=[u for u,_ in MATH_ORDER]
for k,v in out.items():
    if 'units' not in v:
        seen=[]
        for it in v['items']:
            if it['u'] not in seen: seen.append(it['u'])
        v['units']=seen
json.dump(out,open('bank.json','w'),ensure_ascii=False,separators=(',',':'))
print(sum(len(v['items']) for v in out.values()))
allq=[(it['q']+'|'+it['p']+'|'+'/'.join(sorted(it['o']))) for v in out.values() for it in v['items']]
d=[k for k,c in Counter(allq).items() if c>1]
print('duplicates',len(d))
for x in d[:10]: print('  DUP',x[:100])
