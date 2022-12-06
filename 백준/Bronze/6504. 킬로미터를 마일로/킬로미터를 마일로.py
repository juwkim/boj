import sys
from bisect import bisect_left
input = sys.stdin.readline

res = [0]
a, b = 0, 1
while b <= 25000:
    a, b = b, a + b
    res.append(b)

for _ in range(int(input())):
    temp = []
    n = int(input())
    idx = bisect_left(res, n)
    while n:
        if res[idx] <= n:
            temp.append(res[idx-1])
            n -= res[idx]
            idx -= 2
        else:
            idx -= 1
    print(sum(temp))