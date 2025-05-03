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
dist = [-1] * (2 * n + 1)
dist[i] = 0
dq = deque([i])
while dq:
    cur = dq.popleft()
    if cur == j:
        break
    for nxt in riffle(cur), scuffle(cur):
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            dq.append(nxt)
print(dist[j])