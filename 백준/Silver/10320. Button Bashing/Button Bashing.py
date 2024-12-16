import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from collections import deque

for _ in range(int(input())):
    n, t = g()
    b = g()
    cnt = [1e9] * 3601
    cnt[0] = 0
    dq = deque([0])
    while dq:
        x = dq.popleft()
        if x == t:
            break
        for i in b:
            nx = max(0, min(x + i, 3600))
            if cnt[nx] == 1e9:
                cnt[nx] = cnt[x] + 1
                dq.append(nx)
    for i in range(t, 3601):
        if cnt[i] != 1e9:
            print(cnt[i], i - t)
            break