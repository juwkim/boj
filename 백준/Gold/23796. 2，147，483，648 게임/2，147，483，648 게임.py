def move(N, lst):
    ans = []
    
    now = lst.pop(0)
    while lst and now == 0:
        now = lst.pop(0)
    while lst:
        new = lst.pop(0)
        if new == 0:
            continue
        else:
            if now == new:
                ans.append(now + new)
                now = -1
            elif now == -1:
                now = new
            else:
                ans.append(now)
                now = new
    if now != -1:
        ans.append(now)
    ans += [0] * (N - len(ans))
    return ans
    

def solve(N, direction):

    if direction == "l":
        for i in range(N):
            board[i] = move(N, board[i])
            
                   
    elif direction == "r":
        for i in range(N):
            board[i] = move(N, board[i][::-1])[::-1]
                
    elif direction == "u":
        for j in range(N):
            moved = move(N, [board[i][j] for i in range(N)])
            for i in range(N):
                board[i][j] = moved[i]
        
    else:
        for j in range(N):
            moved = move(N, [board[i][j] for i in range(N-1, -1, -1)])
            for i in range(N):
                board[N-i-1][j] = moved[i]

N = 8
board = [[*map(int, input().split())] for _ in range(N)]
direction = input()[0].lower()
solve(N, direction)
for line in board:
    print(*line)