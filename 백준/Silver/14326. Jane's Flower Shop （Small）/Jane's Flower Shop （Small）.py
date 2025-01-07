import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    M = int(input())
    C = [*map(int, input().split())]
    C[0] = -C[0]
    lo, hi = -1, 1
    while hi - lo > 1e-9:
        mid = (lo + hi) / 2
        r1 = mid + 1
        cur = 0
        for num in C: cur = cur * r1 + num
        if cur > 0:
            lo = mid
        else:
            hi = mid
    print(f"Case #{tc}: {lo}")