for _ in range(int(input())):
    N = int(input())
    res = []
    while N:
        r, q = divmod(N, 3)
        res.append(q)
        N = r
    print(*res[::-1])