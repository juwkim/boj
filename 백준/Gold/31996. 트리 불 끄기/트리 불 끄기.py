import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())
sys.setrecursionlimit(10**5)

N, a = g()
S = [0] + [int(i) for i in input()]
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y = g()
    tree[x].append(y)
    tree[y].append(x)
visited = bytearray(N + 1)
visited[a] = 1
def dfs(x):
    for y in tree[x]:
        if not visited[y]:
            visited[y] = 1
            S[x] ^= 1
            ans.append(y)
            dfs(y)
            S[y] ^= 1
            ans.append(x)
            if S[y]:
                S[x] ^= 1
                S[y] ^= 1
                ans.append(y)
                ans.append(x)
ans = []
dfs(a)
if S[a]:
    ans.append(tree[a][0])
print(len(ans))
print(*ans)