import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = g()
    graph[u].append(v)
    graph[v].append(u)

ans = 1
visited = bytearray(N + 1)
for i in range(1, N + 1):
    if visited[i]:
        continue
    visited[i] = 1
    st, cnt = [i], 1
    while st:
        u = st.pop()
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = 1
            cnt += 1
            st.append(v)
    ans = (ans * cnt) % 1_000_000_007
print(ans)