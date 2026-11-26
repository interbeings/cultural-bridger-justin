"""문제 그림용 작은 SVG 도우미. 색은 currentColor/CSS 변수로 지정해 밝은·어두운 화면 모두 대응."""
import math

def _n(v):
    s = f"{v:.1f}"
    return s[:-2] if s.endswith(".0") else s

class Plane:
    """좌표평면: 월드 좌표 [x0,x1]×[y0,y1]를 W×H 픽셀에 그린다."""
    def __init__(self, x0, x1, y0, y1, W=300, H=240, pad=18, equal=False):
        self.x0, self.x1, self.y0, self.y1 = x0, x1, y0, y1
        if equal:
            H = int(round(2 * pad + (y1 - y0) / (x1 - x0) * (W - 2 * pad)))
            if H > 320:
                W = int(round(2 * pad + (x1 - x0) / (y1 - y0) * (320 - 2 * pad))); H = 320
        self.W, self.H, self.pad = W, H, pad
        self.items = []
    def X(self, x): return self.pad + (x - self.x0) / (self.x1 - self.x0) * (self.W - 2 * self.pad)
    def Y(self, y): return self.H - self.pad - (y - self.y0) / (self.y1 - self.y0) * (self.H - 2 * self.pad)
    def axes(self, xlab="x", ylab="y", origin=True):
        X0, Y0 = self.X(0), self.Y(0)
        a = 'stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)"'
        self.items.append(f'<line x1="{_n(self.pad-4)}" y1="{_n(Y0)}" x2="{_n(self.W-6)}" y2="{_n(Y0)}" {a}/>')
        self.items.append(f'<line x1="{_n(X0)}" y1="{_n(self.H-self.pad+4)}" x2="{_n(X0)}" y2="8" {a}/>')
        self.items.append(f'<text x="{_n(self.W-10)}" y="{_n(Y0+14)}" class="t">{xlab}</text>')
        self.items.append(f'<text x="{_n(X0+6)}" y="14" class="t">{ylab}</text>')
        if origin: self.items.append(f'<text x="{_n(X0-12)}" y="{_n(Y0+13)}" class="t">O</text>')
        return self
    def curve(self, f, xa=None, xb=None, n=160, cls="c1", dash=False):
        xa = self.x0 if xa is None else xa; xb = self.x1 if xb is None else xb
        pts = []; segs = []
        for i in range(n + 1):
            x = xa + (xb - xa) * i / n
            try: y = f(x)
            except (ZeroDivisionError, ValueError): y = None
            if y is None or not (self.y0 - 2 <= y <= self.y1 + 2):
                if len(pts) > 1: segs.append(pts)
                pts = []; continue
            pts.append(f"{_n(self.X(x))},{_n(self.Y(y))}")
        if len(pts) > 1: segs.append(pts)
        for s in segs:
            self.items.append(f'<polyline points="{" ".join(s)}" class="{cls}"{" stroke-dasharray=\"5 4\"" if dash else ""}/>')
        return self
    def line(self, p, q, cls="c2", dash=False):
        self.items.append(f'<line x1="{_n(self.X(p[0]))}" y1="{_n(self.Y(p[1]))}" x2="{_n(self.X(q[0]))}" y2="{_n(self.Y(q[1]))}" class="{cls}"{" stroke-dasharray=\"5 4\"" if dash else ""}/>')
        return self
    def hline(self, y, dash=True): return self.line((self.x0, y), (self.x1, y), "c3", dash)
    def vline(self, x, dash=True): return self.line((x, self.y0), (x, self.y1), "c3", dash)
    def poly(self, pts, fill=True):
        s = " ".join(f"{_n(self.X(x))},{_n(self.Y(y))}" for x, y in pts)
        self.items.append(f'<polygon points="{s}" class="{"sh" if fill else "c2"}"/>')
        return self
    def circle(self, c, r, cls="c1"):
        rx = r / (self.x1 - self.x0) * (self.W - 2 * self.pad); ry = r / (self.y1 - self.y0) * (self.H - 2 * self.pad)
        self.items.append(f'<ellipse cx="{_n(self.X(c[0]))}" cy="{_n(self.Y(c[1]))}" rx="{_n(rx)}" ry="{_n(ry)}" class="{cls}"/>')
        return self
    def pt(self, p, label="", dx=6, dy=-6, hollow=False):
        self.items.append(f'<circle cx="{_n(self.X(p[0]))}" cy="{_n(self.Y(p[1]))}" r="3" class="{"pth" if hollow else "pt"}"/>')
        if label: self.items.append(f'<text x="{_n(self.X(p[0])+dx)}" y="{_n(self.Y(p[1])+dy)}" class="t">{label}</text>')
        return self
    def text(self, p, s, dx=0, dy=0):
        self.items.append(f'<text x="{_n(self.X(p[0])+dx)}" y="{_n(self.Y(p[1])+dy)}" class="t">{s}</text>'); return self
    def svg(self):
        return wrap(self.W, self.H, "".join(self.items))

STYLE = ('<style>.t{font:12px sans-serif;fill:currentColor}.c1{fill:none;stroke:#ff6b1a;stroke-width:2}.c2{fill:none;stroke:#3b82f6;stroke-width:1.8}'
         '.c3{fill:none;stroke:currentColor;stroke-width:1;opacity:.55}.sh{fill:#ff6b1a;fill-opacity:.18;stroke:#ff6b1a;stroke-width:1.2}'
         '.pt{fill:currentColor}.pth{fill:none;stroke:currentColor;stroke-width:1.4}.bx{fill:none;stroke:currentColor;stroke-width:1.3}</style>')
def wrap(W, H, body):
    return (f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img">{STYLE}'
            '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="currentColor"/></marker></defs>'
            + body + '</svg>')

def venn(counts, labels=("A", "B"), U=True):
    """counts: dict with keys 'a','ab','b','out' (str or number)"""
    W, H = 280, 170
    b = []
    if U:
        b.append(f'<rect x="6" y="6" width="{W-12}" height="{H-12}" rx="6" class="bx"/><text x="14" y="22" class="t">U</text>')
    b.append('<circle cx="110" cy="88" r="58" class="c1"/><circle cx="172" cy="88" r="58" class="c2"/>')
    b.append(f'<text x="70" y="40" class="t">{labels[0]}</text><text x="205" y="40" class="t">{labels[1]}</text>')
    b.append(f'<text x="80" y="93" class="t">{counts.get("a","")}</text><text x="133" y="93" class="t">{counts.get("ab","")}</text><text x="192" y="93" class="t">{counts.get("b","")}</text>')
    if U and "out" in counts: b.append(f'<text x="{W-40}" y="{H-14}" class="t">{counts["out"]}</text>')
    return wrap(W, H, "".join(b))

def grid_roads(Wn, Hn, blocked_edges=(), mark_points=(), cell=36):
    """Wn×Hn 칸 바둑판 도로. blocked_edges: ((x1,y1),(x2,y2)) 공사 중 도로(×표시)."""
    pad = 22; W = Wn * cell + 2 * pad; H = Hn * cell + 2 * pad
    X = lambda x: pad + x * cell; Y = lambda y: H - pad - y * cell
    b = []
    for i in range(Wn + 1): b.append(f'<line x1="{X(i)}" y1="{Y(0)}" x2="{X(i)}" y2="{Y(Hn)}" class="c3" style="opacity:1"/>')
    for j in range(Hn + 1): b.append(f'<line x1="{X(0)}" y1="{Y(j)}" x2="{X(Wn)}" y2="{Y(j)}" class="c3" style="opacity:1"/>')
    for (p, q) in blocked_edges:
        mx, my = (X(p[0]) + X(q[0])) / 2, (Y(p[1]) + Y(q[1])) / 2
        b.append(f'<path d="M{mx-6},{my-6}L{mx+6},{my+6}M{mx-6},{my+6}L{mx+6},{my-6}" stroke="#e5484d" stroke-width="3"/>')
    b.append(f'<circle cx="{X(0)}" cy="{Y(0)}" r="4" class="pt"/><text x="{X(0)-16}" y="{Y(0)+16}" class="t">A</text>')
    b.append(f'<circle cx="{X(Wn)}" cy="{Y(Hn)}" r="4" class="pt"/><text x="{X(Wn)+6}" y="{Y(Hn)-6}" class="t">B</text>')
    for (p, lab) in mark_points:
        b.append(f'<circle cx="{X(p[0])}" cy="{Y(p[1])}" r="4" fill="#3b82f6"/><text x="{X(p[0])+6}" y="{Y(p[1])-6}" class="t">{lab}</text>')
    return wrap(W, H, "".join(b))

def mapping(xs, ys, f):
    """대응 화살표 그림: f는 dict x->y"""
    W = 240; H = 40 + 30 * max(len(xs), len(ys))
    b = ['<ellipse cx="55" cy="{0}" rx="34" ry="{1}" class="bx"/><ellipse cx="185" cy="{0}" rx="34" ry="{1}" class="bx"/>'.format(H / 2 + 6, H / 2 - 10),
         '<text x="48" y="16" class="t">X</text><text x="178" y="16" class="t">X</text>']
    py = lambda i, n: 6 + H / 2 - (n - 1) * 15 + i * 30
    for i, x in enumerate(xs): b.append(f'<text x="50" y="{py(i,len(xs))+4}" class="t">{x}</text>')
    for i, y in enumerate(ys): b.append(f'<text x="180" y="{py(i,len(ys))+4}" class="t">{y}</text>')
    for i, x in enumerate(xs):
        j = ys.index(f[x])
        b.append(f'<line x1="64" y1="{py(i,len(xs))}" x2="172" y2="{py(j,len(ys))}" stroke="#ff6b1a" stroke-width="1.4" marker-end="url(#ah)"/>')
    return wrap(W, H, "".join(b))

def regions(kind, n):
    """색칠 문제용 영역 그림: 'line' 일렬, 'ring' 원형(가운데 없음), 'star' 가운데 + 바깥 부채꼴"""
    W, H = 260, 150; b = []
    if kind == "line":
        w = (W - 20) / n
        for i in range(n): b.append(f'<rect x="{10+i*w:.1f}" y="45" width="{w:.1f}" height="60" class="bx"/><text x="{10+i*w+w/2-5:.1f}" y="80" class="t">{"ABCDEF"[i]}</text>')
    else:
        cx, cy, R, r0 = 130, 75, 68, (26 if kind == "star" else 30)
        for i in range(n if kind == "ring" else n - 1):
            m = n if kind == "ring" else n - 1
            a = 2 * math.pi * i / m - math.pi / 2
            b.append(f'<line x1="{cx+r0*math.cos(a):.1f}" y1="{cy+r0*math.sin(a):.1f}" x2="{cx+R*math.cos(a):.1f}" y2="{cy+R*math.sin(a):.1f}" class="bx"/>')
            am = a + math.pi / m
            b.append(f'<text x="{cx+(R+r0)/2*math.cos(am)-5:.1f}" y="{cy+(R+r0)/2*math.sin(am)+4:.1f}" class="t">{"ABCDEF"[i + (1 if kind=="star" else 0)]}</text>')
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" class="bx"/><circle cx="{cx}" cy="{cy}" r="{r0}" class="bx"/>')
        if kind == "star": b.append(f'<text x="{cx-5}" y="{cy+4}" class="t">A</text>')
    return wrap(W, H, "".join(b))
