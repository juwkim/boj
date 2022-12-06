g = lambda: [*map(int, input().split())]
for cnt in range(1, 1 + int(input())):
    N, K = g()
    ans = 0
    a, b, c, d = [g() for _ in range(4)]
    for i in range(N):
        x1 = a[i]
        for j in range(N):
            x2 = x1 ^ b[j]
            for k in range(N):
                x3 = x2 ^ c[k]
                for l in range(N):
                    x4 = x3 ^ d[l]
                    ans += (K == x4)
    print(f'Case #{cnt}:', ans)