a = lambda a, b: nums[a * N + b]
N, *nums = map(int, open(0).read().split())
px = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    cur = 0
    for j in range(N):
        cur += a(i, j)
        px[i + 1][j + 1] = cur + px[i][j + 1]
ans = -1e9
for i in range(N):
    for j in range(N):
        for k in range(i + 1, N + 1):
            for l in range(j + 1, N + 1):
                ans = max(ans, px[k][l] - px[i][l] - px[k][j] + px[i][j])
print(ans)