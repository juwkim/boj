import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

dq = deque()
for _ in range(int(input())):
    s = input()
    if s[0] == '1':
        dq.appendleft(s[2:])
    elif s[0] == '2':
        dq.append(s[2:])
    elif s[0] == '3':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif s[0] == '4':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif s[0] == '5':
        print(len(dq))
    elif s[0] == '6':
        print(int(len(dq) == 0))
    elif s[0] == '7':
        if dq:
            print(dq[0])
        else:
            print(-1)
    else:
        if dq:
            print(dq[-1])
        else:
            print(-1)