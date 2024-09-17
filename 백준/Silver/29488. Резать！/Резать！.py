n, m, k = map(int, open(0).read().split())
if n * m % k:
    print(-1)
else:
    ans = [[0] * m for _ in range(n)]
    i, j, dj = 0, 0, 1
    for num in range(1, n * m // k + 1):
        for _ in range(k):
            ans[i][j] = num
            j += dj
            if j == m:
                i += 1
                j = m - 1
                dj = -1
            elif j == -1:
                i += 1
                j = 0
                dj = 1
    for row in ans:
        print(*row)