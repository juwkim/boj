def check(board, n):
    s = [n, n, n]
    a = any(board[i:i+3] == s for i in range(0, 9, 3))
    b = any(board[i::3] == s for i in range(3))
    c = board[0::4] == s or board[2:7:2] == s
    return a or b or c
    
board = [0] * 9
start, flag = int(input()), 0
for i in range(9):
    a, b = map(int, input().split())
    board[3*a+b-4] = 1 + (i%2 + start -1) % 2
    if i > 4:
        if check(board, 1):
            flag = 1
            break
        if check(board, 2):
            flag = 2
            break
print(flag)