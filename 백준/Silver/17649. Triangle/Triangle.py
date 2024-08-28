import sys
input = sys.stdin.readline
from math import dist

n, q = map(int, input().split())
a = [[*map(float, input().split())] for _ in range(n)]
b = [[*map(float, input().split())] for _ in range(q)]

ta = [0.0] * n
tb = [(0, 0.0)] * q
ans = [0] * q

for i in range(n):
    for j in range(n):
        ta[j] = dist(a[i], a[j])
    
    for j in range(q):
        tb[j] = (j, dist(a[i], b[j]))

    ta.sort()
    tb.sort(key=lambda x: x[1])

    k1, k2 = 0, 0
    for j in range(q):
        while k2 < n and ta[k2] < tb[j][1] + 1e-4:
            k2 += 1
        while k1 < n and ta[k1] < tb[j][1] - 1e-4:
            k1 += 1
        ans[tb[j][0]] += k2 - k1

for i in range(q):
    for j in range(n):
        ta[j] = dist(b[i], a[j])
    ta.sort()
    k1, k2 = 0, 0
    while k2 < n:
        while k1 < k2 and ta[k1] < ta[k2] - 1e-4:
            k1 += 1
        ans[i] += k2 - k1
        k2 += 1
for i in range(q):
    print(ans[i])