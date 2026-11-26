import cmath, math, itertools
from fractions import Fraction as F
R={}
# 1 R(x)
a=F(3,2); R[0]=a*(4-1)*(4-2)+2*4+1
w=cmath.exp(2j*math.pi/3)
v=w**2026+w**2025+1; R[1]=round((v-2).real,9),round(v.imag-w.imag,9)  # expect value= w+2
R[2]=2*8-3*4+4*2-1
# 4: brute search numeric a,b,c with sum0 sumsq6: a=b=1? choose param
a,b=1.3,0.0; # solve c=-a-b, scale
import random
for _ in range(3):
    a,b=random.random(),random.random();c=-a-b;s=math.sqrt(6/(a*a+b*b+c*c));a,b,c=a*s,b*s,c*s
    print('q4',round(a**4+b**4+c**4,6))
x=(3+math.sqrt(5))/2;print('q5',x**5+x**-5)
# 6 P(x)=(x-1)(x-2)(x-3)+2x
print('q6',4*3*2+10)
z=(1+math.sqrt(3)*1j)/2;print('q7',z**2026+z**-2026)
z=2+3j;print('q8',(z*z).imag)
sols=[s for s in [1,w,w**2]];print('q9',[abs(s*s-s.conjugate()) for s in sols],sols[0]*sols[1]*sols[2])
r1=(3+math.sqrt(5))/2;r2=(3-math.sqrt(5))/2;print('q10',(r1*r1+r1+1)*(r2*r2+r2+1))
print('q11',sum(1/(1+w**k) for k in range(1,13)))
import numpy as np
rt=np.roots([1,-2,3,-4]);a,b,c=rt;print('q12',(a+b)*(b+c)*(c+a))
print('q13',27-1)
# q14 k=-5 tangent
k=-5;print('q14 D',(k+1)**2-(k*k+k-4))
def mn(a): return min(x*x-2*a*x+3 for x in np.linspace(-1,3,40001))
print('q15',[ (aa,round(mn(aa),4)) for aa in [2,-2.5]])
xs=np.linspace(-5,5,200001);print('q16',min(abs(xx*xx-2*xx+5)/math.sqrt(5) for xx in xs))
print('q17',[a for a in range(-20,20) if (a*a-a-6)>=0 and a>1 and 7-a>0])
def cnt(a): return [x for x in range(-10,20) if x*x-5*x+4<=0 and x*x-(a+2)*x+2*a<0]
print('q18',[(a,cnt(a)) for a in [3,4,4.0001,5,1.5,0.5]])
print('q19',len([x for x in range(-20,20) if abs(x-1)+abs(x+3)<=8]))
def ok(k):
    xs=np.linspace(-50,50,20001);return all((k-1)*x*x-2*(k-1)*x+3>0 for x in xs)
print('q20',[k for k in range(-10,10) if ok(k)])
print('q21',sum(1 for p in itertools.permutations(range(1,7),3) if sum(p)%3==0))
c=0
for p in itertools.permutations('BBBGGG'):
    pass
people=['B1','B2','B3','G1','G2','G3']
for p in itertools.permutations(people):
    if any(p[i][0]=='G' and p[i+1][0]=='G' for i in range(5)):continue
    if p[0][0]=='G' and p[5][0]=='G':continue
    c+=1
print('q22',c)
c=0
for t in itertools.combinations(range(8),3):
    if all((t[i]-t[j])%8 not in (1,7) for i in range(3) for j in range(3) if i!=j):c+=1
print('q23',c)
print('q24',sum(1 for x in range(11) for y in range(11) for z in range(11) if x<=y<=z and x+y+z==10))
print('q25',sum(1 for f in itertools.product(range(3),repeat=5) if len(set(f))==3))
A=np.array([[1,2],[3,4]]);B=np.array([[2,0],[1,-1]]);print('q26',(A@B-B@A).sum())
A=np.array([[1,2],[0,1]]);print('q27',sum(np.linalg.matrix_power(A,n) for n in range(1,11)).sum())
A=np.array([[0,1],[2,1]]);print('q28',np.linalg.matrix_power(A,5),'vs',11*A+10*np.eye(2))
P=((2*7+1)/3,(2*-4+2)/3);Q=((2*7-1),(2*-4-2));print('q29',math.dist(P,Q),8*math.sqrt(2))
print('q30',13/3)
print('q31',3/(5/2))
print('q32',13-9)
print('q33',math.sqrt(25-16)*5)
print('q34',0.5*(24/5)*(16/5),192/25)
th=np.linspace(0,2*math.pi,100001);px=3+2*np.cos(th);py=4+2*np.sin(th)
print('q35',min((px+1)**2+py**2+(px-1)**2+py**2))
# 36 apollonius: check point (0,0): PA=2,PB=4 ok; (-8,0): PA=6,PB=12
print('q36',math.dist((0,0),(-2,0))/math.dist((0,0),(4,0)),math.dist((-8,0),(-2,0))/math.dist((-8,0),(4,0)))
a=2+math.sqrt(5);print('q37',abs(-2+a),math.sqrt(5))
print('q38',math.dist((-1,3),(4,-2)),5*math.sqrt(2))
# 39 brute area min: line x/a+y/b=1 tangent incircle center(1,1) r1 with circle inside
best=1e9
for a in np.linspace(2.01,20,4000):
    # solve b s.t. a+b-sqrt(a^2+b^2)=2 -> b=2(a-1)/(a-2)
    b=2*(a-1)/(a-2);best=min(best,a*b/2)
print('q39',best,3+2*math.sqrt(2))
print('q40',17-4)
print('q41',math.comb(6,3))
print('q42',[a for a in range(-5,6) if a-2>=-2 and a+2<=4])
best=min((x+1/y)*(4*y+1/x) for x in np.linspace(.05,5,300) for y in np.linspace(.05,5,300));print('q43',best)
xs=np.linspace(1.0001,20,200000);print('q44',min((xs**2-xs+4)/(xs-1)))
print('q45',2+-1)
print('q46',(4/3)*9-4)
cnt=0
for f in itertools.permutations(range(4)):
    if all(f[f[i]]==i for i in range(4)) and f[0]!=0:cnt+=1
print('q47',cnt)
f=lambda x:(2*x+5)/(x+1);print('q48',-1+2+f(0)+f(2))
def ninter(k):
    # count solutions t>=0 of t^2-t+1+k=0
    D=1-4*(1+k)
    if D<0:return 0
    ts={(1+math.sqrt(D))/2,(1-math.sqrt(D))/2};return len([t for t in ts if t>=-1e-12])
print('q49',[(k,ninter(k)) for k in [-1.01,-1,-0.9,-0.76,-0.75,-0.7]])
k=65/9;x1=(6+math.sqrt(36-4*k))/2;x2=6-x1;print('q50',0.5*abs(x1*(6-x2)-x2*(6-x1)))
