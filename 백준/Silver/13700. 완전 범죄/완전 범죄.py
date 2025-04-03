from collections import deque

N, S, D, F, B, K, *l = map(int, open(0).read().split())
visited = bytearray(N + 1)
visited[S] = 1
for num in l: visited[num] = 1
ans = "BUG FOUND"
dq = deque([(S, 0)])
while dq:
    pos, cnt = dq.popleft()
    if D in (pos + F, pos - B):
        ans = cnt + 1
        break
    if pos + F <= N and not visited[pos + F]:
        visited[pos + F] = 1
        dq.append((pos + F, cnt + 1))
    if pos - B > 0 and not visited[pos - B]:
        visited[pos - B] = 1
        dq.append((pos - B, cnt + 1))
print(ans)