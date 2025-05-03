from collections import deque

def riffle(pos):
    if pos <= n:
        return 2 * pos - 1
    return 2 * (pos - n)

def scuffle(pos):
    if pos & 1:
        return pos + 1
    return pos - 1

n, i, j = map(int, input().split())
visited = [-1] * (2 * n + 1)
visited[i] = 0
dq = deque([i])
ans = -1
while dq:
    cur = dq.popleft()
    if cur == j:
        ans = visited[cur]
        break
    for nxt in riffle(cur), scuffle(cur):
        if visited[nxt] == -1:
            visited[nxt] = visited[cur] + 1
            dq.append(nxt)
print(ans)