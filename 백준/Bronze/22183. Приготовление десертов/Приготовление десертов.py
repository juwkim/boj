g = lambda: [*map(int, input().split())]

n, m, k = g()
board = [[[1] * k for _ in range(m)] for _ in range(n)]
for _ in range(int(input())):
    a, b = g()
    board[a-1][b-1] = [0] * k
for _ in range(int(input())):
    a, b = g()
    for i in range(n):
        board[i][a-1][b-1] = 0
for _ in range(int(input())):
    a, b = g()
    for i in range(m):
        board[a-1][i][b-1] = 0
cnt = 0
for x in range(n):
    for y in range(m):
        for z in range(k):
            cnt += board[x][y][z]
print(cnt)