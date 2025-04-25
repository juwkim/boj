import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for _ in range(int(input())):
    C, M = g()
    graph = [[] for _ in range(C + 1)]
    for _ in range(C - 1):
        C1, C2, D = g()
        graph[C1].append((C2, D))
        graph[C2].append((C1, D))    
    ans = 0
    st = [(1, 0)]
    visited = bytearray(C + 1)
    visited[1] = 1
    while st:
        node, dist = st.pop()
        flag = True
        for neighbor, d in graph[node]:
            if not visited[neighbor]:
                flag = False
                visited[neighbor] = 1
                st.append((neighbor, dist + d))
        if flag:
            ans = max(ans, dist)
    if ans < M:
        ans = -1
    print(ans)