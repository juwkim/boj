for _ in range(int(input())):
    p, d = 0, 0
    for c in input():
        if c == '[':
            d += 1
        else:
            d -= 1
        p = max(p, d)
    print(1 << p)