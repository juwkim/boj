import sys
g = lambda: map(int, sys.stdin.readline().split())

N, Q = g()
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, L = g()
    tree[a].append((b, L))
    tree[b].append((a, L))

for _ in range(Q):
    p1, p2 = map(int, input().split())
    dist = [-1] * (N + 1)
    st = [p1]
    dist[p1] = 0
    while st:
        u = st.pop()
        if u == p2:
            print(dist[p2])
        for v, w in tree[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + w
                st.append(v)