import sys
input = sys.stdin.readline

while True:
    N, B = map(int, input().split())
    if N == B == -1:
        break
    a = [int(input()) for _ in range(N)]
    input()
    lo, hi = 0, max(a)
    while lo + 1 < hi:
        m = (lo + hi) // 2
        if sum((x + m - 1) // m for x in a) <= B:
            hi = m
        else:
            lo = m
    print(hi)