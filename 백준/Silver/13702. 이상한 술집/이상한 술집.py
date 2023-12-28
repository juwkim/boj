import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
mac = sorted(int(input()) for _ in range(N))
l, h = 1, mac[-1] + 1
while l + 1 < h:
    m = (l + h) // 2
    if sum(x // m for x in mac) >= K:
        l = m
    else:
        h = m
print(l)