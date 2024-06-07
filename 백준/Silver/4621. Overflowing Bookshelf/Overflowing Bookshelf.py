import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

tc = 1
while (s:=int(input())) != -1:
    dq = deque()
    total = 0
    while (cmd:=input()) != 'E':
        if cmd[0] == 'A':
            _, id, w = cmd.split()
            id, w = int(id), int(w)
            dq.appendleft((id, w))
            total += w
            while total > s:
                total -= dq.pop()[1]
        else:
            _, id = cmd.split()
            id = int(id)
            for i in range(len(dq)):
                if dq[i][0] == id:
                    total -= dq[i][1]
                    del dq[i]
                    break
    ans = [id for id, _ in dq]
    print(f"PROBLEM {tc}:", *ans)
    tc += 1