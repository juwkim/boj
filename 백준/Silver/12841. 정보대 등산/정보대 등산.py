import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n = int(input())
d, l, r = g(), g(), g()
pxl, pxr = [0] * n, [0] * n
for i in range(1, n):
    pxl[i] = pxl[i - 1] + l[i - 1]
    pxr[i] = pxr[i - 1] + r[i - 1]
num, dist = 1, 1e11
for i in range(n):
    p = pxl[i] + d[i] + pxr[-1] - pxr[i]
    if p < dist:
        num, dist = i + 1, p
print(num, dist)