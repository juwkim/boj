n, *nums = map(int, open(0).read().split())
graph = [[(i + n) % (2 * n)] for i in range(2 * n)]
pos = [-1] * (n + 1)
for i, v in enumerate(nums):
    if pos[v] == -1:
        pos[v] = i
    else:
        graph[i].append(pos[v])
        graph[pos[v]].append(i)
color = [-1] * (2 * n)
def dfs(v, c):
    color[v] = c
    return all(color[nxt] != c and (color[nxt] != -1 or dfs(nxt, c ^ 1)) for nxt in graph[v])
ans = 1
for i in range(2 * n):
    if color[i] == -1:
        if not dfs(i, 0):
            ans = 0
            break
        ans <<= 1
print(ans)