import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left

l, n = [1], 1
while n < 5 * 10**9:
    n += sum(map(int, str(n)))**2
    l.append(n)

for _ in range(int(input())):
    M = int(input())
    print(("NIE", "TAK")[M == l[bisect_left(l, M)]])