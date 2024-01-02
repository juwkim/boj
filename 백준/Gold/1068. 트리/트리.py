import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
tree = [[] for _ in range(N)]
parent = g()
root = -1
for i, num in enumerate(parent):
    if num == -1:
        root = i
    else:
        tree[num].append(i)

def dfs(node):
    if not tree[node]:
        return 1
    return sum(dfs(child) for child in tree[node])

node = int(input())
ans = dfs(root) - dfs(node)
if len(tree[parent[node]]) == 1:
    ans += 1
print(ans)