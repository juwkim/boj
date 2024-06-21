for l in map(str.rstrip, [*open(0)][:-1]):
    a = [[], []]
    for c in l:
        a[c.isupper()].append(c)
    WFF, u = a
    if not WFF:
        print("no WFF possible")
    else:
        for c in u:
            if c == 'N':
                WFF.append(f"{c}{WFF.pop()}")
            elif len(WFF) >= 2:
                WFF.append(f"{c}{WFF.pop()}{WFF.pop()}")
        print(WFF[-1])