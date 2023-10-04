import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def check(mid):
    pricipal = N
    for _ in range(M):
        interest = (pricipal * R + 99) // 100
        pricipal -= mid - interest
        if pricipal <= 0:
            break
    return pricipal <= 0

for line in sys.stdin:
    N, M, R = map(int, line.split())
    l, h = N // M - 1, 2 * N
    while l + 1 < h:
        mid = (l + h) // 2
        if check(mid):
            h = mid
        else:
            l = mid
    print(h)
