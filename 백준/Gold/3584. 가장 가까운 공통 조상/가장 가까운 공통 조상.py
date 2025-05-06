import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for _ in range(int(input())):
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    inbound = [0] * (N + 1)
    for _ in range(N - 1):
        a, b = g()
        inbound[b] += 1
        graph[a].append(b)        
    idx = 1
    while inbound[idx]:
        idx += 1        
    lca = [[0, 0] for _ in range(N + 1)] # parent, depth
    visited = bytearray(N + 1)
    visited[idx] = 1
    st = [(idx, 0)]
    while st:
        node, depth = st.pop()
        for child in graph[node]:
            if not visited[child]:
                visited[child] = 1
                lca[child][0] = node
                lca[child][1] = depth + 1
                st.append((child, depth + 1))
    a, b = g()
    if lca[a][1] < lca[b][1]:
        a, b = b, a
    while lca[a][1] > lca[b][1]:
        a = lca[a][0]
    while a != b:
        a = lca[a][0]
        b = lca[b][0]
    print(a)