import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = -1
for i in range(1, N + 1):
    visited = bytearray(N + 1)
    visited[i] = 1
    st = [i]
    while st:
        node = st.pop()
        for child in graph[node]:
            if visited[child] == 0:
                visited[child] = 1
                st.append(child)
    if visited.count(1) == N:
        ans = i
        break
print(ans)