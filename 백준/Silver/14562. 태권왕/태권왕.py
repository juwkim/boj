import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    S, T = map(int, input().split())
    dq = deque([(S, T, 0)])
    while dq:
        s, t, cnt = dq.popleft()
        if s == t:
            print(cnt)
            break
        if s * 2 <= t + 3:
            dq.append((s * 2, t + 3, cnt + 1))
        if s + 1 <= t:
            dq.append((s + 1, t, cnt + 1))