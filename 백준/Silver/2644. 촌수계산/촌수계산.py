g = lambda: [*map(int, input().split())]

from collections import deque
N = int(input())
a, b = g()
buf = [[] for _ in range(N + 1)]
for _ in range(int(input())):
    s, t = g()
    buf[s].append(t)
    buf[t].append(s)

visited = [0 for _ in range(N + 1)]

visited[a] = 1
dq = deque([(a, 1)])
ans = -1
while dq:
    num, d = dq.pop()
    for val in buf[num]:
        if val == b:
            ans = d
            break
        if visited[val] == 0:
            visited[val] = 1
            dq.append((val, d + 1))
print(ans)