import sys
from collections import deque
input = sys.stdin.readline

n = 1000000
dist = [0] * (n + 1)
dist[1] = 1
dq = deque([1])
while dq:
    u = dq.popleft()
    for v in (u + 1, int(str(u)[::-1])):
        if v <= n and dist[v] == 0:
            dist[v] = dist[u] + 1
            dq.append(v)
for tc in range(1, 1 + int(input())):
    print(f"Case #{tc}: {dist[int(input())]}")