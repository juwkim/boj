for cnt in range(1, 1 + int(input())):
    M = int(input())
    board = [['.'] * M for _ in range(M)]
    for _ in range(int(input())):
        s, *l, c = input().split()
        x, y, w, h = map(int, l)
        if s == 'Filled':
            for i in range(x-1, x+w-1):
                for j in range(y-1, y+h-1):
                    board[i][j] = c
        else:
            board[x-1][y-1:y+h-1] = [c] * h
            for i in range(x, x+w-2):
                board[i][y-1] = c
                board[i][y+h-2] = c
            board[x+w-2][y-1:y+h-1] = [c] * h
    print(f'Case {cnt}:')
    for line in [*zip(*board)][::-1]:
        print(*line, sep='')