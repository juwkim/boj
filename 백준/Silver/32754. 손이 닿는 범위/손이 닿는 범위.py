import sys
g = lambda: map(int, sys.stdin.readline().split())

ans = 0
N, R = g()
for _ in range(N):
    x1, y1, x2, y2, x3, y3, x4, y4 = g()
    c1, c2 = (x1 + x2 + x3 + x4) / 4, (y1 + y2 + y3 + y4) / 4
    R1 = ((x1 - c1) ** 2 + (y1 - c2) ** 2)**.5
    if c1 ** 2 + c2 ** 2 <= (R + R1) ** 2:
        ans += 1
print(ans)