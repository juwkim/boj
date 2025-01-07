import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M, K = g()
st = [int(input()) for _ in range(M)]
graph = [[] for _ in range(N + 1)]
for _ in range(K):
    a, b = g()
    graph[a].append(b)
    graph[b].append(a)
ans, visited = M, bytearray(N + 1)
for num in st:
    visited[num] = 1
while st:
    cur = st.pop()
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = 1
            ans += 1
            st.append(nxt)
print(ans)