for _ in range(int(input())):
    s = input()
    x, y = [*map(int, s)], [0] * len(s)
    l = sum(x) // 2
    for i in range(len(s)):
        if x[i] >= l:
            y[i] = l
            x[i] -= l
            break
        else:
            l -= x[i]
            y[i] = x[i]
            x[i] = 0
    print(int("".join(map(str, x))), int("".join(map(str, y))))