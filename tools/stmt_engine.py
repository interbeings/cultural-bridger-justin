"""진술 은행 → 보기형/옳은 것/옳지 않은 것 문항 조합 생성기"""
import random, itertools
COMB = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄱ, ㄴ', 'ㄱ, ㄷ', 'ㄴ, ㄷ', 'ㄱ, ㄴ, ㄷ']

def make(bank, per_unit, seed, src_by_lvl, subject_topic=""):
    """bank: {unit: {"T":[str], "F":[(str, 바른설명)], "lvl":int, "topic": "~에 대한 설명"}}"""
    rng = random.Random(seed); out = []
    for unit, d in bank.items():
        T, Fs = d["T"], d["F"]; topic = d.get("topic", unit + "에 대한 설명")
        seen = set(); tries = 0; made = 0
        while made < per_unit and tries < per_unit * 50:
            tries += 1
            kind = rng.choices(["bogi", "right", "wrong"], weights=[5, 2, 2])[0]
            if kind == "bogi":
                k = rng.choice([1, 2, 2, 2, 3])  # 참 진술 수
                if k > len(T) or 3 - k > len(Fs): continue
                ts = rng.sample(T, k); fs = rng.sample(Fs, 3 - k)
                items = [(s, True, None) for s in ts] + [(s, False, c) for s, c in fs]
                rng.shuffle(items)
                key = ("b",) + tuple(sorted(x[0] for x in items))
                if key in seen: continue
                lab = "ㄱㄴㄷ"
                ans = ", ".join(lab[i] for i, x in enumerate(items) if x[1])
                if not ans: continue
                i = COMB.index(ans); st = rng.choice([s for s in range(3) if s <= i < s + 5])
                opts = COMB[st:st + 5]
                q = f"{topic}으로 옳은 것만을 <보기>에서 있는 대로 고른 것은?\n" + "\n".join(f"{lab[j]}. {x[0]}" for j, x in enumerate(items))
                exp = " ".join(f"{lab[j]}({'○' if x[1] else '×'})" + ("" if x[1] else f": {x[2]}") for j, x in enumerate(items))
                lvl = d.get("lvl", 3) + (1 if k == 3 or k == 1 and rng.random() < .3 else 0)
            elif kind == "right":
                t = rng.choice(T); fs = rng.sample(Fs, 4)
                key = ("r", t) + tuple(sorted(f[0] for f in fs))
                if key in seen: continue
                opts = [t] + [f[0] for f in fs]; rng.shuffle(opts); ans = t
                q = f"{topic}으로 옳은 것은?"
                exp = "오답 풀이: " + " / ".join(f"'{f[0][:18]}…' → {f[1]}" for f in fs)
                lvl = d.get("lvl", 3)
            else:
                f = rng.choice(Fs); ts = rng.sample(T, 4)
                key = ("w", f[0]) + tuple(sorted(ts))
                if key in seen: continue
                opts = [f[0]] + ts; rng.shuffle(opts); ans = f[0]
                q = f"{topic}으로 옳지 않은 것은?"
                exp = f"틀린 진술: {f[1]}"
                lvl = d.get("lvl", 3)
            seen.add(key)
            lvl = min(lvl, 4)
            out.append(dict(unit=unit, lvl=lvl, src=src_by_lvl(lvl), q=q, opts=opts, ans=ans, exp=exp))
            made += 1
    return out
