import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque

F, S, G, U, D = g()

dq = deque([(S, 0)])
visited = [False] * (F + 1)
visited[S] = True
ans = "use the stairs"
while dq:
    cur, cnt = dq.popleft()
    if cur == G:
        ans = cnt
        break
    for nxt in (cur + U, cur - D):
        if 1 <= nxt <= F and not visited[nxt]:
            visited[nxt] = True
            dq.append((nxt, cnt + 1))
print(ans)