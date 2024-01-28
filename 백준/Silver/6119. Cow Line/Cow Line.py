import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

dq = deque()
cow = 1
for _ in range(int(input())):
    s = input()
    if s == "A L":
        dq.appendleft(cow)
        cow += 1
    elif s == "A R":
        dq.append(cow)
        cow += 1
    else:
        _, di, K = s.split()
        if di == "L":
            for _ in range(int(K)):
                dq.popleft()
        else:
            for _ in range(int(K)):
                dq.pop()
print(*dq)