def read_int():
    yield from map(int, open(0).read().split())

f = read_int()
n, m, s = next(f), next(f), next(f)
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = next(f), next(f)
    adj[a].append(b)
    adj[b].append(a)
visited = bytearray(n)
visited[s] = 1
st = [s]
while st:
    v = st.pop()
    for u in adj[v]:
        if not visited[u]:
            visited[u] = 1
            st.append(u)
print(("no", "yes")[all(visited)])