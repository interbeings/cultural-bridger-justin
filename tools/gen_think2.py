import random
from common import num_opts, uniq
rng=random.Random(777);OUT=[]
def add(*r):
    u,l,s,q,o,a,e=r;assert a in o and uniq(o) and len(o)==5;OUT.append(dict(unit=u,lvl=l,src=s,q=q,opts=o,ans=a,exp=e))
seen=set()
def go(fn,n):
    k=0;c=0
    while c<n and k<5000:
        k+=1;r=fn()
        if r and r[3] not in seen: seen.add(r[3]);add(*r);c+=1
def box():
    a,b,c=sorted(rng.sample(range(2,9),3))
    k=rng.choice([0,1,2,3])
    v={3:8,2:4*((a-2)+(b-2)+(c-2)),1:2*((a-2)*(b-2)+(b-2)*(c-2)+(a-2)*(c-2)),0:(a-2)*(b-2)*(c-2)}[k]
    if k==3 and rng.random()<.7: return None
    # brute check
    cnt=0
    for x in range(a):
        for y in range(b):
            for z in range(c):
                f=(x in(0,a-1))+(y in(0,b-1))+(z in(0,c-1))
                cnt+= f==k
    assert cnt==v
    kk="하나도 칠해지지 않은" if k==0 else f"정확히 {k}면이 칠해진"
    o,ans=num_opts(v,rng,lo=0)
    return ("공간 지각",3,"수리논리",f"가로 {a}, 세로 {b}, 높이 {c}인 직육면체의 겉면을 모두 칠한 뒤 한 변이 1인 정육면체로 모두 잘랐다. {kk} 정육면체의 개수는?",o,ans,
            "꼭짓점 8개는 3면, 모서리(꼭짓점 제외)는 2면, 면의 안쪽은 1면, 내부는 0면이 칠해진다 → "+str(v)+".")
def stair():
    n=rng.randint(3,9);kind=rng.choice(["stack","visible"])
    if kind=="stack":
        v=n*(n+1)//2;q=f"정육면체를 1층에 {n}개, 2층에 {n-1}개, …, 맨 위층에 1개를 한쪽 끝에 맞춰 계단 모양으로 쌓았다. 사용한 정육면체의 개수는?";e=f"1+2+…+{n}={v}"
    else:
        v=n**3-(n-1)**3;q=f"한 변의 길이가 1인 정육면체 {n**3}개를 쌓아 만든 큰 정육면체를 한 꼭짓점 쪽에서 비스듬히 바라볼 때(세 면이 보임) 보이는 작은 정육면체의 개수는?";e=f"전체 {n}³에서 보이지 않는 ({n}−1)³을 빼면 {v}"
    o,ans=num_opts(v,rng,lo=1)
    return ("공간 지각",3,"수리논리",q,o,ans,e+".")
def faces():
    solids=[("정사면체",4,6,4),("정육면체",6,12,8),("정팔면체",8,12,6),("정십이면체",12,30,20),("정이십면체",20,30,12),("삼각기둥",5,9,6),("사각뿔",5,8,5),("오각기둥",7,15,10),("육각뿔",7,12,7),("육각기둥",8,18,12)]
    nm,F_,E,V=rng.choice(solids);kind=rng.choice(["F","E","V","sum"])
    if kind=="sum": v=V-E+F_;w="(꼭짓점 수)−(모서리 수)+(면의 수)"
    else: v={"F":F_,"E":E,"V":V}[kind];w={"F":"면의 수","E":"모서리의 수","V":"꼭짓점의 수"}[kind]
    o,ans=num_opts(v,rng,lo=0)
    return ("공간 지각",2,"수리논리",f"{nm}의 {w}는?",o,ans,f"{nm}: 면 {F_}, 모서리 {E}, 꼭짓점 {V} (오일러 공식 V−E+F=2).")
go(box,30);go(stair,10);go(faces,14)
if __name__=="__main__":
    print(len(OUT));print(OUT[0]['q'],OUT[0]['opts'],OUT[0]['ans'])
