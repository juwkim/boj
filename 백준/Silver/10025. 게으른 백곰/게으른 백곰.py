import sys

input = lambda: sys.stdin.readline().rstrip()
mis = lambda: [*map(int, input().split())]

N, K = mis()
if K >= 500000:
    ans = 0
    for _ in range(N):
        g, x = mis()
        ans += g
else:
    line = [0] * 1000001
    for _ in range(N):
        g, x = mis()
        line[x] = g
    px = [0] * 1000002
    for i in range(1, 1000002):
        px[i] = px[i - 1] + line[i - 1]

    ans = 0
    for i in range(K, 1000001 - K):
        ans = max(ans, px[i + K + 1] - px[i - K])
print(ans)