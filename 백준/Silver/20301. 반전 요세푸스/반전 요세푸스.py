import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque

N, K, M = g()
di = -K+1
dq = deque(range(1, N + 1))
for i in range(N):
    if i and i % M == 0:
        di = 1 - di
    dq.rotate(di)
    print(dq.popleft())