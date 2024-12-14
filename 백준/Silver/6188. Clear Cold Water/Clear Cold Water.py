import sys
g = lambda: map(int, sys.stdin.readline().split())

N, C = g()
tree = [() for _ in range(N + 1)]
for _ in range(C):
    E, B1, B2 = g()
    tree[E] = B1, B2
dist = [0] * (N + 1)
st = [(1, 1)]
while st:
    node, d = st.pop()
    dist[node] = d
    for child in tree[node]:
        st.append((child, d + 1))
print(*dist[1:], sep='\n')