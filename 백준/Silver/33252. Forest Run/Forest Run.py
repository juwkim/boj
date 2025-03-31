import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

n, e = g()
entrances = g()
tree = [[]] + [g()[1:] for _ in range(n)]
ans = 0
for entrance in entrances:
    st = [(entrance, 0)]
    while st:
        node, depth = st.pop()
        if tree[node]:
            for child in tree[node]:
                st.append((child, depth + 1))
        else:
            ans += depth * 2
print(ans)