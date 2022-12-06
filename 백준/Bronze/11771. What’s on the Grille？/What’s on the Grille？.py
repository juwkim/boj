n = int(input())
grille = [input() for _ in range(n)]
board = [[' '] * n for _ in range(n)]
msg = [*input()]
try:
    for _ in range(4):
        for i in range(n):
            for j in range(n):
                if grille[i][j] == '.':
                    board[i][j] = msg.pop(0)
        grille = [i[::-1] for i in zip(*grille)]
    
    decoded = ''.join([''.join(i) for i in board])
    if ' ' in decoded:
        print('invalid grille')
    else:
        print(decoded)
except:
    print('invalid grille')