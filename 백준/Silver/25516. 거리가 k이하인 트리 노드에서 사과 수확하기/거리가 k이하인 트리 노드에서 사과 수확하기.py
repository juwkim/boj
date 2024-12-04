import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from collections import deque

n, k = g()
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    p, c = g()
    tree[p].append(c)
apple = g()
ans = 0
dq = deque([(0, 0)])
while dq:
    cur, cnt = dq.popleft()
    ans += apple[cur]
    if cnt == k:
        continue
    for nxt in tree[cur]:
        dq.append((nxt, cnt + 1))
print(ans)