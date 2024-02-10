for _ in range(int(input())):
    input()
    a, b, c = 0, 0, 0
    for p in map(float, input().split()):
        a, b, c = b, c, max(a + p, c)
    print(c)