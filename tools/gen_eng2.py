import importlib,re,random,itertools
rng=random.Random(99)
sets=[]
for i in range(1,40):
    try: m=importlib.import_module(f"eset{i}")
    except ModuleNotFoundError: continue
    sets+=getattr(m,f"SETS{i}")
FIX={23:"disrupts",27:"return",30:"lower",31:"less accurately",32:"difficult",36:"never produced",43:"inconvenient",44:"minority",46:"enormous",47:"process",34:"careful"}
def clean(n,s):
    p=s['passage']
    voc=[q for q in s['qs'] if q[0]=='어휘'][0];pos=voc[2][0]
    m=re.search(re.escape(pos)+r"([A-Za-z\-']+)",p);wrong=m.group(1)
    cor=FIX.get(n) or re.findall(r"\(([A-Za-z][A-Za-z \-]*)",voc[3])[0].split('/')[0]
    p=p.replace(pos+wrong,cor)
    blank=[q for q in s['qs'] if q[0]=='빈칸'][0][2][0]
    p=p.replace("_______",blank)
    for c in "①②③④⑤": p=p.replace(c,"")
    assert "_" not in p
    return p
def sents(p):
    p=p.replace("\n"," ")
    out=re.split(r'(?<=[.!?])\s+(?=[A-Z\'"])',p)
    return [x.strip() for x in out if x.strip()]
OUT=[]
for n,s in enumerate(sets):
    ss=sents(clean(n,s))
    if len(ss)<8: continue
    # 순서 배열: 단락 첫 부분 7문장
    st=0 if rng.random()<.5 else max(0,len(ss)-7)
    win=ss[st:st+7]
    given=win[0];chunks=[" ".join(win[1:3])," ".join(win[3:5])," ".join(win[5:7])]
    labels=["(A)","(B)","(C)"];perm=list(range(3));rng.shuffle(perm)
    if perm==[0,1,2]: perm=[1,2,0]
    shown={labels[i]:chunks[perm[i]] for i in range(3)}
    inv={perm[i]:labels[i] for i in range(3)}
    ans="-".join(inv[j] for j in range(3))
    allp=["-".join(p) for p in itertools.permutations(labels)]
    opts=sorted([ans]+rng.sample([x for x in allp if x!=ans],4))
    passage=given+"\n"+"\n".join(f"{l} {shown[l]}" for l in labels)
    OUT.append(dict(unit="글의 순서·흐름",lvl=4,src="수능 변형",q="주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",passage=passage,opts=opts,ans=ans,
        exp=f"원래 흐름: {ans}. 지시어·연결어와 내용의 전개(원인→결과, 일반→예시 등)를 따라가면 순서가 정해진다. (장문 세트 지문 변형)"))
    # 문장 삽입: 7문장 창 중 3~6번째 하나를 빼서 위치 찾기
    st2=rng.randint(0,len(ss)-7);win=ss[st2:st2+7]
    k=rng.randint(2,5)  # 빠질 문장 index in win (2..5)
    removed=win[k];rest=win[:k]+win[k+1:]   # 6 sentences → 5 gaps after sentence 0..4
    parts=[rest[0]]
    marks="①②③④⑤"
    for g in range(5): parts.append(f"( {marks[g]} ) {rest[g+1]}")
    ansm=marks[k-1]
    OUT.append(dict(unit="글의 순서·흐름",lvl=4,src="수능 변형",q=f"글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?\n[주어진 문장] {removed}",passage=" ".join(parts),opts=list(marks),ans=ansm,
        exp=f"주어진 문장은 {ansm} 자리에 들어가야 앞뒤 문장의 지시어·연결어와 논리가 이어진다. (장문 세트 지문 변형)"))
if __name__=="__main__":
    print(len(OUT));print(OUT[0]['passage'][:600]);print(OUT[0]['ans']);print(OUT[1]['q']);print(OUT[1]['passage'][:500],OUT[1]['ans'])
