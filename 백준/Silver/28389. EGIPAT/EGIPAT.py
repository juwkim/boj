import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [[*input()] for _ in range(N)]
x, y = -1, -1
for i in range(N):
    for j in range(M):
        if a[i][j] == 'P':
            x, y = i, j
            break
    if x != -1:
        break
name = "gore", "desno", "dolje", "lijevo"
while True:
    a[x][y] = '.'
    for i, (nx, ny) in enumerate(((x-1, y), (x, y+1), (x+1, y), (x, y-1))):
        if 0 <= nx < N and 0 <= ny < M and a[nx][ny] == 'x':
            print(name[i])
            x, y = nx, ny
            break
    else:
        break