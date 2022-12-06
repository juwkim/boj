g = lambda: [*map(int, input().split())]

P, N = g()
board = [-1] * (P + 1)
for i in range(N):
    idx = int(input())
    color = i & 1
    board[idx] = color
    
    lidx = idx - 1
    while lidx >= 1 and board[lidx] == 1 - color:
        lidx -= 1
    ridx = idx + 1
    while ridx <= P and board[ridx] == 1 - color:
        ridx += 1
    
    if lidx != 0 and board[lidx] == color:
        board[lidx+1:idx] = [-1] * (idx - lidx - 1)
    if ridx != P + 1 and board[ridx] == color:
        board[idx+1:ridx] = [-1] * (ridx - idx - 1)
print(board.count(0), board.count(1))