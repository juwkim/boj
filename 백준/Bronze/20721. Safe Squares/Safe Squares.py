board = [[1] * 8 for _ in range(8)]

for i in range(8):
    line = input()
    buf = [j for j in range(8) if line[j] == 'R']
    if buf:
        board[i] = [0] * 8
        for idx in buf:
            for i in range(8):
                board[i][idx] = 0
print(sum(sum(line) for line in board))