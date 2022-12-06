def check(lst):
    for i in range(3):
        if lst[i]:
            if lst[i] == lst[i+1]:
                return False
        else:
            return not sum(lst[i+1:])
    return True
    

def move(direction):
    global score
    if direction == "L":
        i = 0
        while i < 4:
            j = 0
            merge = 0
            while j < 3:
                shift = True
                if board[i][j]:
                    if board[i][j] == board[i][j+1]:
                        board[i][j+1] += board[i][j]
                        board[i][j] = 0
                        score += board[i][j+1]
                        merge = j + 1
                    else:
                        shift = False

                if shift:
                    for k in range(j, 3):
                        board[i][k] = board[i][k+1]
                    board[i][3] = 0
                

                if check(board[i][merge:]):
                    break
                if board[i][j] == 0:
                    j = 0
                else:
                    j += 1
            i += check(board[i][merge:])
            
                    
    elif direction == "R":
        i = 0
        while i < 4:
            j = 3
            merge = 3
            while j > 0:
                shift = True
                if board[i][j]:
                    if board[i][j] == board[i][j-1]:
                        board[i][j-1] += board[i][j]
                        board[i][j] = 0
                        score += board[i][j-1]
                        merge = j - 1
                    else:
                        shift = False

                if shift:
                    for k in range(j, 0, -1):
                        board[i][k] = board[i][k-1]
                    board[i][0] = 0
                if check(board[i][merge::-1]):
                    break
                if board[i][j] == 0:
                    j = 3
                else:
                    j -= 1
            i += check(board[i][merge::-1])
                
    elif direction == "U":
        j = 0
        while j < 4:
            i = 0
            merge = 0
            while i < 3:
                shift = True
                if board[i][j]:
                    if board[i][j] == board[i+1][j]:
                        board[i+1][j] += board[i][j]
                        board[i][j] = 0
                        score += board[i+1][j]
                        merge = i + 1
                    else:
                        shift = False

                if shift:
                    for k in range(i, 3):
                        board[k][j] = board[k+1][j]
                    board[3][j] = 0
                
                if check([board[i][j] for i in range(merge, 4)]):
                    break
                if board[i][j] == 0:
                    i = 0
                else:
                    i += 1
            j += check([board[i][j] for i in range(merge, 4)])
    else:
        j = 0
        while j < 4:
            i = 3
            merge = 3
            while i > 0:
                shift = True
                if board[i][j]:
                    if board[i][j] == board[i-1][j]:
                        board[i-1][j] += board[i][j]
                        board[i][j] = 0
                        score += board[i-1][j]
                        merge = i - 1
                    else:
                        shift = False

                if shift:
                    for k in range(i, 0, -1):
                        board[k][j] = board[k-1][j]
                    board[0][j] = 0
                
                if check([board[i][j] for i in range(merge, -1, -1)]):
                    break
                if board[i][j] == 0:
                    i = 3
                else:
                    i -= 1
            j += check([board[i][j] for i in range(merge, -1, -1)])

score = int(input())
game = input()
board = [*map(int, input().split())]
board = [board[i:i+4] for i in range(0, 16, 4)]

for i in range(0, len(game), 4):
    if i > 36:
        break
    direction, num, x, y = game[i:i+4]
    move(direction)
    board[int(x)][int(y)] = int(num)

print(score)