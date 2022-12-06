def check(N, lst):
    for i in range(N-1):
        if lst[i]:
            if lst[i] == lst[i+1]:
                return False
        else:
            return not sum(lst[i+1:])
    return True
    

def move(N, direction):
    global score
    if direction == "l":
        i = 0
        while i < N:
            j = 0
            merge = 0
            while j < N-1:
                shift = True
                if board[i][j]:
                    if board[i][j] == board[i][j+1]:
                        board[i][j+1] += board[i][j]
                        board[i][j] = 0
                        merge = j + 1
                    else:
                        shift = False

                if shift:
                    for k in range(j, N-1):
                        board[i][k] = board[i][k+1]
                    board[i][N-1] = 0
                

                if check(N, board[i][merge:]):
                    break
                if board[i][j] == 0:
                    j = 0
                else:
                    j += 1
            i += check(N, board[i][merge:])
            
                    
    elif direction == "r":
        i = 0
        while i < N:
            j = N-1
            merge = N-1
            while j > 0:
                shift = True
                if board[i][j]:
                    if board[i][j] == board[i][j-1]:
                        board[i][j-1] += board[i][j]
                        board[i][j] = 0
                        merge = j - 1
                    else:
                        shift = False

                if shift:
                    for k in range(j, 0, -1):
                        board[i][k] = board[i][k-1]
                    board[i][0] = 0
                if check(N, board[i][merge::-1]):
                    break
                if board[i][j] == 0:
                    j = N-1
                else:
                    j -= 1
            i += check(N, board[i][merge::-1])
                
    elif direction == "u":
        j = 0
        while j < N:
            i = 0
            merge = 0
            while i < N-1:
                shift = True
                if board[i][j]:
                    if board[i][j] == board[i+1][j]:
                        board[i+1][j] += board[i][j]
                        board[i][j] = 0
                        merge = i + 1
                    else:
                        shift = False

                if shift:
                    for k in range(i, N-1):
                        board[k][j] = board[k+1][j]
                    board[N-1][j] = 0
                
                if check(N, [board[i][j] for i in range(merge, N)]):
                    break
                if board[i][j] == 0:
                    i = 0
                else:
                    i += 1
            j += check(N, [board[i][j] for i in range(merge, N)])
    else:
        j = 0
        while j < N:
            i = N-1
            merge = N-1
            while i > 0:
                shift = True
                if board[i][j]:
                    if board[i][j] == board[i-1][j]:
                        board[i-1][j] += board[i][j]
                        board[i][j] = 0
                        merge = i - 1
                    else:
                        shift = False

                if shift:
                    for k in range(i, 0, -1):
                        board[k][j] = board[k-1][j]
                    board[0][j] = 0
                
                if check(N, [board[i][j] for i in range(merge, -1, -1)]):
                    break
                if board[i][j] == 0:
                    i = N-1
                else:
                    i -= 1
            j += check(N, [board[i][j] for i in range(merge, -1, -1)])

for case in range(1, 1 + int(input())):
    N, direction = input().split()
    N = int(N)
    board = [[*map(int, input().split())] for _ in range(N)]
    move(N, direction[0])
    print(f'Case #{case}:')
    for line in board:
        print(*line)