import sys
g = lambda: map(int, sys.stdin.readline().split())

m, n = g()
px = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    cur = 0
    for j, c in enumerate(g(), 1):
        cur += c
        px[i][j] = cur + px[i - 1][j]
ans = 0
for i in range(m):
    for j in range(n):
        for k in range(i + 1, m + 1):
            for l in range(j + 1, n + 1):
                num = px[k][l] - px[i][l] - px[k][j] + px[i][j]
                if num > 10:
                    break
                if num == 10:
                    ans += 1
print(ans)