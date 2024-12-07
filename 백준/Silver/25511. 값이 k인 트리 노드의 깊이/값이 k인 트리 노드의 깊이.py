import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

n, k = g()
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    p, c = g()
    graph[p].append(c)

i = g().index(k)
st = [(0, 0)]
while st:
    cur, d = st.pop()
    if cur == i:
        break
    for nxt in graph[cur]:
        st.append((nxt, d + 1))
print(d)