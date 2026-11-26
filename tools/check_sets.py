import importlib,re,sys
from collections import Counter
files=[f"eset{i}" for i in range(1,40)]
allsets=[]
for f in files:
    try: m=importlib.import_module(f)
    except ModuleNotFoundError: continue
    for k,v in vars(m).items():
        if k.startswith("SETS"): allsets+= [(f,s) for s in v]
pos=Counter();bad=0;words=[]
for f,s in allsets:
    p=s['passage'];w=len(p.split());words.append(w)
    for c in "①②③④⑤":
        if p.count(c)!=1: print("CIRC",f,c,p[:40]);bad+=1
    if p.count("_______")!=1: print("BLANK",f,p[:40]);bad+=1
    if len(s['qs'])!=5: print("NQ",f);bad+=1
    for t,q,o,e in s['qs']:
        if len(set(o))!=5: print("DUPOPT",f,t);bad+=1
        if t=="어휘": pos[o[0]]+=1
print(len(allsets),"sets",bad,"problems",pos,"words min/avg/max",min(words),sum(words)//len(words),max(words))
