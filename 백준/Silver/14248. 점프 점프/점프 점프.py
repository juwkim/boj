from collections import deque

n, *A, s = map(int, open(0).read().split())
dq = deque([s - 1])
visited = bytearray(n)
visited[s - 1] = 1
while dq:
    a = dq.popleft()
    for b in (a - A[a], a + A[a]):
        if 0 <= b < n and not visited[b]:
            visited[b] = 1
            dq.append(b)
print(sum(visited))