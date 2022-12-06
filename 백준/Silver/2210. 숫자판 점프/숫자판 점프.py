Map = [input().split() for _ in range(5)]
buf = [None for _ in range(6)]
ans = set()
def dfs(i, j, d):
    if d == 6:
        ans.add(''.join(buf))
        return
    
    buf[d] = Map[i][j]
    for s, t in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
        if 0 <= s < 5 and 0 <= t < 5:
            dfs(s, t, d + 1)

for i in range(5):
    for j in range(5):
        dfs(i, j, 0)

print(len(ans))