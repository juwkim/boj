import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
dist2 = lambda a, b: (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

n, p, s = g()
graph = [[] for _ in range(n)]
points = [g() for _ in range(n)]
for i in range(n - 1):
    x1, y1 = points[i]
    for j in range(i + 1, n):
        x2, y2 = points[j]
        d2 = dist2((x1, y1), (x2, y2))
        if d2 <= s * s:
            graph[i].append(j)
            graph[j].append(i)
    
visited = bytearray(n)
visited[p - 1] = 1
st = [p - 1]
ans = s
while st:
    v = st.pop()
    ans = max(ans, s + dist2(points[p - 1], points[v])**.5)
    for u in graph[v]:
        if not visited[u]:
            visited[u] = 1
            st.append(u)
print(ans)