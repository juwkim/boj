for tc, l in enumerate([*open(0)][:-1], 1):
    *l, s = l.split()
    l = [*map(int, l)]
    num = int(float(s[1:]) * 100)
    coins, imbalance = "", 1e9
    for a in range(min(l[0], num // 200), -1, -1):
        num1 = num - 200 * a
        for b in range(min(l[1], num1 // 100), -1, -1):
            num2 = num1 - 100 * b
            for c in range(min(l[2], num2 // 50), -1, -1):
                num3 = num2 - 50 * c
                for d in range(min(l[3], num3 // 20), -1, -1):
                    num4 = num3 - 20 * d
                    e = num4 // 10
                    if e <= l[4] and num4 % 10 == 0:
                        cnt = [x - y for x, y in zip(l, [a, b, c, d, e])]
                        m = min(cnt)
                        cur_imbalance = sum((x - m) ** 2 for x in cnt)
                        if cur_imbalance < imbalance:
                            coins, imbalance = (a, b, c, d, e), cur_imbalance
    if imbalance == 1e9:
        ans = "not possible"
    else:
        p = []
        for coin, weight in zip(coins, ("$2", "$1", "50c", "20c", "10c")):
            if coin:
                p.append(f"{coin} {weight}")
        if len(p) >= 2:
            last = p.pop()
            p[-1] += f" and {last}"
        ans = ", ".join(p) + " coin(s)"    
    print(f"Problem #{tc}: {ans}")