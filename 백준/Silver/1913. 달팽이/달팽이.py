N = int(input())
num = int(input())
margin = [[-1] * (N + 2)]
Map = margin + [[-1] + [0] * N + [-1] for _ in range(N)] + margin

x, y, d = 1, 1, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for cur in range(N * N, 0, -1):
    if cur == num:
        s, t = x, y
    
    Map[x][y] = cur
    if Map[x + dx[d]][y + dy[d]]:
        d = (d + 1) % 4
    x += dx[d]
    y += dy[d]
for i in range(1, 1 + N):
    print(*Map[i][1:-1])
print(s, t)