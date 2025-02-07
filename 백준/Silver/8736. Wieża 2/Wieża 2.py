import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from bisect import bisect_left

n, m = g()
a = g()
min = a[0]
for i in range(1, n):
    if a[i] < min:
        a[i] = min
    else:
        min = a[i]
prv = n
for b in g():
    num = bisect_left(a, b, hi=prv)
    print(num, end=' ')
    prv = max(0, num - 1)