import sys

input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N = int(input())
dq = deque([input().split() for _ in range(N)])
for _ in range(N >> 1):
    _, cnt = dq.popleft()
    dq.rotate(1 - int(cnt))
    dq.popleft()
print(dq[0][0])