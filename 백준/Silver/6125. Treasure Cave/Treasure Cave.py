import sys
g = lambda: map(int, sys.stdin.readline().split())

P, NS, T = g()
tree = [() for _ in range(P + 1)]
parent = [0] * (P + 1)
for _ in range(NS):
    N, B1, B2 = g()
    tree[N] = B1, B2
    parent[B1] = parent[B2] = N
st, path = [1], []
while st:
    node = st.pop()
    while path and parent[node] != path[-1]:
        path.pop()
    path.append(node)
    if node == T:
        break
    st.extend(tree[node])
print(len(path), *path)