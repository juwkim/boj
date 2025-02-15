import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
dist2 = lambda p, q: (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

def solve(cnt):
    points = [g() for _ in range(cnt)]
    bn, bcnt = bytearray(n), bytearray(cnt)
    ans = 0
    for dis, i, j in sorted((dist2(points[i], (x[j], y[j])), j, i) for i in range(cnt) for j in range(n)):
        if bn[i] or bcnt[j]: continue
        bn[i], bcnt[j] = 1, 1
        ans += dis ** .5
    return ans

n, m, k = g()
x, y = zip(*[g() for _ in range(n)])
print(solve(m) + solve(k))