import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque
for _ in range(int(input())):
    input()
    dq = deque()
    for c in input().split():
        if not dq or c <= dq[0]:
            dq.appendleft(c)
        else:
            dq.append(c)
    print(*dq, sep='')