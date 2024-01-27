import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

cow = [[0] * 1001 for _ in range(1001)]
board = [[0] * 1003 for _ in range(1003)]
ans = 0
for _ in range(int(input())):
    x, y = g()
    cow[x][y] = 1
    ans += board[x][y] == 3
    for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
        board[nx][ny] += 1
        if cow[nx][ny]:
            ans += (board[nx][ny] == 3) - (board[nx][ny] == 4)
    print(ans)