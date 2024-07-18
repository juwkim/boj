import sys
input = sys.stdin.readline
from math import inf
g = lambda: [*map(int, input().split())]

n = int(input())
j, dj, s, ds = g(), g(), g(), g()
for i in range(n):
    j[i] -= s[i]
    dj[i] -= ds[i]
l, r = 0, inf
ans = "Strong is dark side of the force."
for i in range(n):
    if j[i] < 0 and dj[i] <= 0:
        break
    if j[i] >= 0 and dj[i] < 0:
        r = min(r, (j[i] // abs(dj[i]) + 1))
    elif j[i] <= 0 and dj[i] > 0:
        l = max(l, (abs(j[i]) - 1) // dj[i] + 1)
else:
    if l < r:
        ans = l
print(ans)