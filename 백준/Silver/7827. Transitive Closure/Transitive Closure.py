import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for _ in range(int(input())):
    N, M = g()
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = g()
        graph[A].append(B)
    ans = 0
    for i in range(1, N + 1):
        visited = bytearray(N + 1)
        visited[i] = 1
        st = [i]
        while st:
            node = st.pop()
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = 1
                    st.append(next_node)
        ans += visited.count(1) - 1
    print(ans)