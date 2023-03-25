while (n := input()) != '0 0 0':
    a, b, c = map(int, n.split())
    if a == 0 and b == 0:
        print(0)
    else:
        for _ in range(c):
            a, b = b, a + b
        print(b)