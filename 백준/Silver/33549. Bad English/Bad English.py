def solve():
    l = []
    for s in input().split():
        word = []
        for c in s:
            if c.isalpha():
                word.append(c.lower())
        if word:
            l.append("".join(word))
    return l

r = solve()
t = solve()
d = {a: b for a, b in zip(input().split(), input().split())}
if len(r) == len(t) and all(d.get(t[i], None) == r[i] for i in range(len(t))):
    print("STONECOAL")
else:
    print("VALID")