import sys
g = lambda: map(int, sys.stdin.readline().split())

W, H, K, T = g()
ans = 1
for _ in range(K):
    x, y = g()
    xmax, xmin = min(x + T, W), max(x - T, 1)
    ymax, ymin = min(y + T, H), max(y - T, 1)
    ans = ans * (xmax - xmin + 1) * (ymax - ymin + 1) % 998244353
print(ans)