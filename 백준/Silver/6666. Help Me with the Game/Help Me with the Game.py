white_big, white_pawn = [], []
black_big, black_pawn = [], []
for i in range(8):
    input()
    line = input()
    for j in range(2, len(line), 4):
        if line[j].isalpha():
            x = chr((j - 2) // 4 + 97)
            y = str(8 - i)
            if line[j].isupper():
                if line[j] == 'P':
                    white_pawn.append(x + y)
                else:
                    white_big.append(line[j] + x + y)
            else:
                if line[j] == 'p':
                    black_pawn.append(x + y)
                else:
                    black_big.append(line[j].upper() + x + y)
white_big.sort(key=lambda x: ('KQRBN'.index(x[0]), int(x[2]), x[1]))
black_big.sort(key=lambda x: ('KQRBN'.index(x[0]), -int(x[2]), x[1]))
white_pawn.sort(key=lambda x: (int(x[1]), x[0]))
black_pawn.sort(key=lambda x: (-int(x[1]), x[0]))
print('White:', ','.join(white_big + white_pawn))
print('Black:', ','.join(black_big + black_pawn))