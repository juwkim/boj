import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque

input()
dq = deque()
for i, op in enumerate(g()[::-1], 1):
    if op == 1:
        dq.appendleft(i)
    elif op == 2:
        dq.insert(1, i)
    elif op == 3:
        dq.append(i)
print(*dq)