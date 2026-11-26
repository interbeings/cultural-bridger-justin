# 생성 문항 수치 재검증: 문제 문자열에서 매개변수를 다시 읽어 brute-force
import re, math, cmath, numpy as np
from fractions import Fraction as F
import gen_math as g
def num(s): return float(F(s.replace('−','-')))
bad=0;checked=0
for o in g.OUT:
    q=o['q'].replace('−','-');a=o['ans']
    try:
        m=re.match(r'삼차방정식 (.+)=0의 세 근을 α, β, γ라 할 때, (.+)의 값은',q)
        if m:
            poly=m.group(1).replace('x³','*x**3').replace('x²','*x**2').replace('x','*x')
            # 계수 추출
            cs=np.polyfit(np.arange(-3,4),[eval(poly.replace('+*','+').replace('-*','-').lstrip('*'),{'x':xv}) for xv in range(-3,4)],3)
            r=np.roots(cs);al,be,ga=r
            expr={'(α+β)(β+γ)(γ+α)':(al+be)*(be+ga)*(ga+al),'(1+α)(1+β)(1+γ)':(1+al)*(1+be)*(1+ga),'(2-α)(2-β)(2-γ)':(2-al)*(2-be)*(2-ga)}[m.group(2)]
            checked+=1
            if abs(expr-num(a))>1e-6: bad+=1;print('BAD',o['q'],a,expr)
        m=re.match(r'곡선 y=x² 위의 점과 직선 y=(-?\d*)x(-\d+) 사이',q)
        if m:
            mm=int(m.group(1) or 1);c=int(m.group(2))
            xs=np.linspace(-10,10,400001);d=np.min(np.abs(mm*xs-xs**2+c)/math.sqrt(mm*mm+1))
            aa=a.replace('−','-');v=eval(re.sub(r'(\d*)√(\d+)',lambda t:f"({t.group(1) or 1}*math.sqrt({t.group(2)}))",aa))
            checked+=1
            if abs(d-v)>1e-6: bad+=1;print('BAD',q,a,d)
        m=re.match(r'점 P\((\d+),0\)에서 원 x²\+y²=(\d+)에',q)
        if m:
            d=int(m.group(1));r=math.sqrt(int(m.group(2)))
            x0=r*r/d;h=math.sqrt(r*r-x0*x0);area=h*(d-x0)
            checked+=1
            if abs(area-num(a))>1e-6: bad+=1;print('BAD',q,a,area)
        m=re.match(r'두 점 A\((-?\d+),0\), B\((-?\d+),0\)에 대하여 PA:PB=1:(\d)',q)
        if m:
            p,qq,k=map(int,m.groups())
            # 내분/외분점
            i1=(k*p+qq)/(k+1)  # PA:PB=1:k → P closer to A
            e1=(qq-k*p)/(1-k)
            checked+=1
            if abs(abs(i1-e1)/2-num(a))>1e-9: bad+=1;print('BAD',q,a)
        m=re.match(r'x>(\d+)일 때, \((.+)\)/\(x-\d+\)의 최솟값',q)
        if m:
            c=int(m.group(1));e=m.group(2).replace('x²','x**2').replace('x','*x').replace('+*','+').replace('-*','-').lstrip('*')
            e=re.sub(r'(\d)\*x',r'\1*x',e)
            xs=np.linspace(c+1e-4,c+60,600001);v=np.min(eval(e,{'x':xs})/(xs-c))
            checked+=1
            if abs(v-num(a))>1e-4: bad+=1;print('BAD',q,a,v)
        m=re.match(r'양수 x, y에 대하여 \(x\+(\d+)/y\)\((\d*)y\+(\d+)/x\)',q)
        if m:
            A=int(m.group(1));B=int(m.group(2) or 1);C=int(m.group(3))
            t=np.linspace(0.01,30,300001) # t=xy
            v=np.min(B*t+C+A*B+A*C/t)
            checked+=1
            if abs(v-num(a))>1e-4: bad+=1;print('BAD',q,a,v)
        m=re.match(r'(-?\d+)≤x≤(-?\d+)에서 이차함수 f\(x\)=x²-2ax\+(\d+)의 최솟값이 (-?\d+)',q)
        if m:
            p,qq,c,mn=map(int,m.groups());xs=np.linspace(p,qq,4001);sols=[]
            for av in np.arange(-40,40,0.0005):
                pass
            sols=[]
            grid=np.arange(-30,30,1/2520)
            vals=np.array([np.min(xs*xs-2*av*xs+c) for av in grid[::7]])
            # find roots of vals-mn by sign change
            gg=grid[::7];s=0
            for i in range(len(gg)-1):
                if (vals[i]-mn)*(vals[i+1]-mn)<=0 and vals[i]!=vals[i+1]: s+=gg[i]
            checked+=1
            if abs(s-num(a))>0.05: bad+=1;print('BAD',q,a,s)
        m=re.match(r'함수 y=\((.+)\)/\((.+)\)의 그래프가 점 \(p,q\)에 대하여 대칭이고, (-?\d+)≤x≤(-?\d+)',q)
        if m:
            nu=m.group(1).replace('x','*x').replace('+*','+').replace('-*','-').lstrip('*');de=m.group(2).replace('x','*x').lstrip('*')
            lo,hi=int(m.group(3)),int(m.group(4))
            f=lambda x:eval(nu,{'x':x})/eval(de,{'x':x})
            xs=np.linspace(lo,hi,10001);fv=f(xs)
            # 대칭점: 점근선
            c=-eval(de,{'x':0});
            aa=(f(1e7))
            v=c+aa+fv.max()+fv.min()
            checked+=1
            if abs(v-num(a))>1e-3: bad+=1;print('BAD',q,a,v)
    except Exception as ex:
        print('ERR',q,ex);bad+=1
print('checked',checked,'bad',bad)
