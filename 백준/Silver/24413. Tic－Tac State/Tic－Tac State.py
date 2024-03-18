for _ in range(int(input())):
    state = bytearray(19)
    i = 0
    for c in map(int, input()[::-1]):
        for j in range(3):
            state[i] = (c >> j) & 1
            i += 1
            if i == 19:
                break
        if i == 19:
            break
    board = [["" for _ in range(3)] for _ in range(3)]
    progress = False
    for i in range(3):
        for j in range(3):
            if state[i * 3 + j] == 0:
                progress = True
                continue
            if state[i * 3 + j + 9]:
                board[i][j] = 'X'
            else:
                board[i][j] = 'O'
    board += [*map(list, zip(*board))] + [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
    if any(r == ['O', 'O', 'O'] for r in board):
        print("O wins")
    elif any(r == ['X', 'X', 'X'] for r in board):
        print("X wins")
    elif progress:
        print("In progress")
    else:
        print("Cat's")