data = [*map(int, open(0).read().split()[::-1])]

V, E = data.pop(), data.pop()
graph = [[] for _ in range(V)]
for _ in range(E):
    A, B = data.pop(), data.pop()
    graph[A].append(B)
group = []
for i in range(V):
    visited = bytearray(V)
    visited[i] = 1
    st = [i]
    while st:
        node = st.pop()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = 1
                st.append(nxt)
    group.append(visited)
for _ in range(data.pop()):
    X, Y = data.pop(), data.pop()
    print(group[X][Y])