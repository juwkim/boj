import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M, H = g()
board = [g() for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(len(board[i])):
        if board[i][j] >= H:
            ans += 1
            continue
        if all(board[k][j] < H for k in range(i)):
            continue
        if all(board[k][j] < H for k in range(i + 1, N)):
            continue
        if all(board[i][k] < H for k in range(j)):
            continue
        if all(board[i][k] < H for k in range(j + 1, len(board[i]))):
            continue
        ans += 1
print(ans)