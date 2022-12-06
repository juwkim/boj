g = lambda: [*map(int, input().split())]

N = int(input())
Map = [g() for _ in range(N)]
res = []
for i in range(1, N-1):
    tmp = []
    for j in range(1, N-1):
        num = Map[i][j] + Map[i+1][j] + Map[i][j+1] + Map[i-1][j] + Map[i][j-1]
        tmp.append(num)
    res.append(tmp)

ans = 1e9
visited = [bytearray(N-2) for _ in range(N-2)]
dr = [-2, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 2]
dc = [0, -1, 0, 1, -2, -1, 0, 1, 2, -1, 0, 1, 0]
def solve(idx, step, num):
    global ans
    if step == 3:
        ans = min(ans, num)
        return
    
    if idx == (N - 2) * (N - 2):
        return
    
    solve(idx + 1, step, num)
    r, c = divmod(idx, N - 2)
    if visited[r][c] == 0:
        check = []
        for i in range(13):
            x, y = r + dr[i], c + dc[i]
            if 0 <= x < N - 2 and 0 <= y < N - 2 and visited[x][y] == 0:
                check.append((x, y))
                visited[x][y] = 1
        solve(idx + 1, step + 1, num + res[r][c])
        
        for x, y in check:
            visited[x][y] = 0    

solve(0, 0, 0)
print(ans)