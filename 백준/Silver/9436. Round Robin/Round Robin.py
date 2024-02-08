import sys
from collections import deque

while True:
    try:
        N, T = map(int, sys.stdin.readline().split())
        dq = deque([0] * N)
        while True:
            dq[0] += 1
            for _ in range(T - 1):
                dq.rotate(-1)
                dq[0] += 1
            dq.popleft()
            if len(set(dq)) == 1:
                break
        print(len(dq), dq[0])
    except:
        break