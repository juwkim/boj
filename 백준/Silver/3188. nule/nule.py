import sys
input = sys.stdin.readline

def cnt(x, p):
    cnt = 0
    while x and x % p == 0:
        x //= p
        cnt += 1
    return cnt

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]
dp2 = [[1e9]*n for _ in range(n)]
dp5 = [[1e9]*n for _ in range(n)]
dp2[0][0] = cnt(board[0][0], 2)
dp5[0][0] = cnt(board[0][0], 5)
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            continue
        c2 = cnt(board[i][j], 2)
        c5 = cnt(board[i][j], 5)
        if i > 0:
            dp2[i][j] = min(dp2[i][j], dp2[i-1][j] + c2)
            dp5[i][j] = min(dp5[i][j], dp5[i-1][j] + c5)
        if j > 0:
            dp2[i][j] = min(dp2[i][j], dp2[i][j-1] + c2)
            dp5[i][j] = min(dp5[i][j], dp5[i][j-1] + c5)
print(min(dp2[-1][-1], dp5[-1][-1]))