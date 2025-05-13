import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
graph = defaultdict(list)
elements = {}
lowers = set()
for _ in range(N):
    x, _, s = input().split()
    graph[s].append(x)
    if s.isupper():
        elements[s] = set()
    else:
        lowers.add(s)
    if x.isupper():
        elements[x] = set()
    else:
        lowers.add(x)
for c in lowers:
    st = [c]
    visited = set()
    while st:
        node = st.pop()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                st.append(nxt)
                if node.islower():
                    elements[nxt].add(node)
                else:
                    elements[nxt].update(elements[node])
for c in sorted(c for c in elements if c.isupper()):
    print(f"{c} = {{{','.join(sorted(elements[c]))}}}")