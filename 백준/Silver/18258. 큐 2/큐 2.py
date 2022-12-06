import sys
input = lambda: sys.stdin.readline().rstrip('\n')
from collections import deque
dq = deque()
for _ in range(int(input())):
    s = input()
    cmd = s[1]
    if cmd == 'u':
        dq.append(s.split()[1])
    elif cmd == 'o':
        print(dq.popleft() if dq else -1)
    elif cmd == 'i':
        print(len(dq))
    elif cmd == 'm':
        print(+(len(dq) == 0))
    elif cmd == 'r':
        print(dq[0] if dq else -1)
    else:
        print(dq[-1] if dq else -1)