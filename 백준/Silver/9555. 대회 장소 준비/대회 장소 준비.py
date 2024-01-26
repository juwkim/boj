import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N, M = g()
    board = [g() + [0] for _ in range(N)] + [[0] * (M + 1)]
    check = bytearray(101)
    for i in range(N):
        for j in range(M):
            if board[i][j] == -1:
                continue
            for s, t in ((i, j + 1), (i + 1, j), (i + 1, j + 1)):
                if board[i][j] == board[s][t]:
                    check[board[i][j]] = 1
            if j:
                if board[i][j] == board[i + 1][j - 1]:
                    check[board[i][j]] = 1                
    print(sum(check))