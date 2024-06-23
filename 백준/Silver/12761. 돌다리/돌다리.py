from collections import deque

A, B, N, M = map(int, input().split())
dq = deque([(N, 0)])
visited = bytearray(100001)
while dq:
    x, cnt = dq.popleft()
    if x == M:
        print(cnt)
        break    
    for nx in (x + 1, x - 1, x + A, x - A, x + B, x - B, x * A, x * B):
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = True
            dq.append((nx, cnt + 1))