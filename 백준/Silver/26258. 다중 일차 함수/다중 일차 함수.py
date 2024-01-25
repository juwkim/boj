import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left

x, y = [], []
for _ in range(int(input())):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
for _ in range(int(input())):
    i = bisect_left(x, float(input()))
    ans = (y[i] > y[i - 1]) - (y[i] < y[i - 1])
    print(ans)