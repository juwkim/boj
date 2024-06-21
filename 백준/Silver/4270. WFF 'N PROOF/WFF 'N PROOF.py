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
                s = WFF.pop()
                WFF.append(f"{c}{s}")
            elif len(WFF) >= 2:
                s = WFF.pop()
                t = WFF.pop()
                WFF.append(f"{c}{s}{t}")
        print(WFF[-1])