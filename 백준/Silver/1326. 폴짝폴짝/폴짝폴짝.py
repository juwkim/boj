from collections import deque

n, *A, a, b = map(int, open(0).read().split())
dq = deque([(a - 1, 0)])
visited = bytearray(n)
visited[a - 1] = 1
ans = -1
while dq:
    x, cnt = dq.popleft()
    if x == b - 1:
        ans = cnt
        break
    for nx in range(x + A[x], n, A[x]):
        if not visited[nx]:
            visited[nx] = 1
            dq.append((nx, cnt + 1))
    for nx in range(x - A[x], -1, -A[x]):
        if not visited[nx]:
            visited[nx] = 1
            dq.append((nx, cnt + 1))
print(ans)