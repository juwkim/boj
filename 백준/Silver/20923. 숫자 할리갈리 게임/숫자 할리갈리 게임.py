from collections import deque
import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
do, su = deque(), deque()
for _ in range(N):
    a, b = g()
    do.append(a)
    su.append(b)

do_dq, su_dq = deque(), deque()
win = -1
for i in range(M):
    if i & 1:
        su_dq.append(su.pop())
        if not su or su_dq[-1] == 5:
            win = 0
        elif do_dq and do_dq[-1] + su_dq[-1] == 5:
            win = 1
    else:
        do_dq.append(do.pop())
        if not do or (su_dq and do_dq[-1] + su_dq[-1] == 5):
            win = 1
        elif do_dq[-1] == 5:
            win = 0
    if win == 1:
        win = -1
        while do_dq:
            su.appendleft(do_dq.popleft())
        while su_dq:
            su.appendleft(su_dq.popleft())
    elif win == 0:
        win = -1
        while su_dq:
            do.appendleft(su_dq.popleft())
        while do_dq:
            do.appendleft(do_dq.popleft())
    elif not do or not su:
        break
if len(do) > len(su):
    print('do')
elif len(do) < len(su):
    print('su')
else:
    print('dosu')