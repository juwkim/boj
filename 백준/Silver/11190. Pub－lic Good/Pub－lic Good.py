import sys
g = lambda: map(int, sys.stdin.readline().split())

n, m = g()
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = g()
    graph[x - 1].append(y - 1)
    graph[y - 1].append(x - 1)

color = [-1] * n
for i in range(n):
    if color[i] == -1:
        if not graph[i]:
            break
        color[i] = 0
        st = [(i, 0)]
        while st:
            node, col = st.pop()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = col ^ 1
                    st.append((neighbor, col ^ 1))

if all(c != -1 for c in color):
    for i in range(n):
        print(("house", "pub")[color[i]], end=" ")
else:
    print("Impossible")