import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N = int(input())
    lo, hi = 1, N
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid * (mid + 1) // 2 <= N:
            lo = mid
        else:
            hi = mid
    print(lo)