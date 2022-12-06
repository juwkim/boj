n = int(input())

ans = []
board = [['.'] * n for _ in range(n)]
full = ['W' for _ in range(n)]
w = 0
for i in range(n):
    s = input()
    ans.append(list(s))
    for j in range(n):
        if s[j] == 'W':
            w += 1
            board[i] = full
            
            for k in range(n):
                board[k][j] = 'W'
            break

for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            ans[i][j] = 'W'
            
            board[i] = full
            for k in range(n):
                board[k][j] = 'W'            
            
            w += 1
        
        if w == n:
            break

for line in ans:
    print(*line, sep='')