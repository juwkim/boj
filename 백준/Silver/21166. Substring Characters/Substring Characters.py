def period(s):
    return frozenset(s)

for s in map(str.rstrip, open(0)):
    n = len(s)
    full_period = period(s)
    seen = set()
    for i in range(n - 1):
        for j in range(i + 1, n + 1):
            if j - i == n:
                continue
            sub = s[i:j]
            if sub not in seen and period(sub) == full_period and period(sub[1:]) != full_period and period(sub[:-1]) != full_period:
                seen.add(sub)
    print(len(seen))