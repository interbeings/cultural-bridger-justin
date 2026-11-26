from fractions import Fraction as F
import math, random

def fr(v):
    """Fraction/int -> 문자열 (음수는 −)"""
    v = F(v)
    s = str(v.numerator) if v.denominator == 1 else f"{abs(v.numerator)}/{v.denominator}"
    if v.denominator != 1 and v < 0: s = "−" + s
    return s.replace("-", "−")

def simp_sqrt(n):
    """n -> (a,b) with sqrt(n)=a*sqrt(b)"""
    a, b = 1, n
    k = 2
    while k * k <= b:
        while b % (k * k) == 0:
            b //= k * k; a *= k
        k += 1
    return a, b

def rad(coef, q):
    """coef*sqrt(q) 문자열 (coef: Fraction)"""
    coef = F(coef)
    a, b = simp_sqrt(q)
    coef *= a
    if b == 1: return fr(coef)
    num, den = coef.numerator, coef.denominator
    sgn = "−" if num < 0 else ""
    num = abs(num)
    top = (f"{num}√{b}" if num != 1 else f"√{b}")
    return sgn + (top if den == 1 else f"{top}/{den}")

def num_opts(ans, rng, step=None, lo=None):
    """정답 ans(Fraction/int) 주변의 그럴듯한 오답 4개 + 정답 → 정렬된 5개 문자열"""
    ans = F(ans)
    if step is None:
        if ans.denominator != 1:
            step = F(1, ans.denominator) * rng.choice([1, 2])
        else:
            m = abs(ans)
            step = 1 if m < 15 else (2 if m < 40 else (5 if m < 200 else 10))
    pos = rng.randrange(5)
    vals = [ans + (k - pos) * step for k in range(5)]
    if lo is not None and min(vals) < lo:
        vals = [lo + k * step for k in range(5)]
        if ans not in vals:
            vals = [ans + k * step for k in range(5)]
    return [fr(v) for v in vals], fr(ans)

def uniq(opts):
    return len(set(opts)) == len(opts)
