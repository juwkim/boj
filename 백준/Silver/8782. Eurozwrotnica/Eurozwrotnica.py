import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    N = int(input())    
    dq, target = deque(), 1
    ans = "TAK"
    for train in map(int, input().split()):
        used = False
        while dq and dq[0] == target or train == target:
            if dq and dq[0] == target:
                dq.popleft()
                target += 1
            elif train == target:
                used = True
                target += 1
        if used:
            continue
        if dq and dq[-1] > train:
            ans = "NIE"
            break
        dq.append(train)
    print(ans)