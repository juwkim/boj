import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

dq = deque(range(1, int(input()) + 1))
front = 1
for _ in range(int(input())):
    if input() == 'A':
        if front:
            dq.rotate(-1)
        else:
            dq.rotate(1)
    else:
        front ^= 1
if front:
    print(*dq, sep='\n')
else:
    print(*reversed(dq), sep='\n')