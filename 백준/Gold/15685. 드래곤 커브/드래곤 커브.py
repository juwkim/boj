import sys
input = lambda: sys.stdin.readline().rstrip()

board = [[0] * 101 for _ in range(101)]
for _ in range(int(input())):
    x, y, d, g = map(int, input().split())
    buf = [d]
    for _ in range(g):
        buf.extend((i + 1) % 4 for i in buf[::-1])
    board[x][y] = 1
    for i in buf:
        match i:
            case 0:
                x += 1
            case 1:
                y -= 1
            case 2:
                x -= 1
            case 3:
                y += 1
        board[x][y] = 1
ans = sum(all(board[p][q] for p, q in ((i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1))) for i in range(100) for j in range(100))
print(ans)