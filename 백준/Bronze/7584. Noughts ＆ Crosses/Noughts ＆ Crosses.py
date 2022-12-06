while (s:= input()) != '#':
    first, *l = s.split()
    if len(l) == 9:
        cur = int(first == 'O')
        board = [[-1] * 3 for _ in range(3)]
        for num in l:
            r, c = divmod(int(num) - 1, 3)
            board[r][c] = cur
            cur ^= 1
        board += [list(i) for i in zip(*board)]
        board += [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
        if [0, 0, 0] in board:
            print('X')
        elif [1, 1, 1] in board:
            print('O')
        else:
            print('Draw')
    else:
        print('OX'[((first == 'O') + len(l)) % 2])