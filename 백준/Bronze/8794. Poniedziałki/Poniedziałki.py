g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N, M, L = g()
    r, q = divmod(N, M)
    if any(L <= i <= L + q - 1 for i in [1, M + 1]):
        r += 1
    print(r)