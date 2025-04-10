K, N, M = map(int, input().split())
cows = [int(input()) for _ in range(K)]
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
cnt = [0] * (N + 1)
for cow in cows:
    visited = bytearray(N + 1)
    st = [cow]
    visited[cow] = True
    cnt[cow] += 1
    while st:
        node = st.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                cnt[neighbor] += 1
                st.append(neighbor)
print(cnt.count(K))