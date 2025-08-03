n = int(input())
path = []
def dfs(remain, start):
    if remain == 0:
        print("+".join(map(str, path)))
        return
    for x in range(start, remain+1):
        if len(path) >= 2 and path[-1] * 2 == path[-2] + x:
            continue
        path.append(x)
        dfs(remain - x, x + 1)
        path.pop()
dfs(n, 1)