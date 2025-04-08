import sys
from collections import deque
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
dq = deque([g() for _ in range(N)])
cnt = [0] * (M + 1)
for P, W in dq:
    cnt[P] += 1
ans = 0
for curw in range(M, 0, -1):
    d = deque()
    while cnt[curw]:
        P, W = dq.popleft()
        ans += W
        if P != curw:
            dq.append((P, W))
            continue
        cnt[curw] -= 1
        l = []
        while d and d[-1][1] < W:
            l.append(d.pop())
        d.append((P, W))
        while l:
            P, W = l.pop()
            ans += 2 * W
            d.append((P, W))
print(ans)