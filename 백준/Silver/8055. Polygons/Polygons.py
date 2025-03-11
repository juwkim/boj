from collections import defaultdict, deque

neighbor = defaultdict(list)
nodes = []
n = int(input())
for i in range(n - 2):
    a, b, c = sorted(map(int, input().split()))
    nodes.append((a, b, c))
    neighbor[(a, b)].append(i)
    neighbor[(a, c)].append(i)
    neighbor[(b, c)].append(i)

visited = bytearray(n - 2)
visited[0] = 1

def bfs(edge):
    if len(neighbor[edge]) == 1:
        return 0

    cnt = 0
    node = neighbor[edge][1]
    dq = deque([node])
    visited[node] = 1
    while dq:
        cur = dq.popleft()
        cnt += 1
        a, b, c = nodes[cur]
        for edge in (a, b), (a, c), (b, c):
            for nxt in neighbor[edge]:
                if not visited[nxt]:
                    visited[nxt] = 1
                    dq.append(nxt)
    return cnt

p = bfs(nodes[0][:2])
q = bfs(nodes[0][1:])
r = n - 3 - p - q

if p + q + r == max(p, q, r) or p + q + r & 1:
    ans = "TAK"
else:
    ans = "NIE"

print(ans)