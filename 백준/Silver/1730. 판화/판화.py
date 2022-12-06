N = int(input())
Map = [['.'] * N for _ in range(N)]
i, j = 0, 0
for cmd in input():
    if cmd == 'U':
        if i:
            if Map[i][j] == '.':
                Map[i][j] = '|'
            elif Map[i][j] == '-':
                Map[i][j] = '+'
            i -= 1
            if Map[i][j] == '.':
                Map[i][j] = '|'
            elif Map[i][j] == '-':
                Map[i][j] = '+'
    elif cmd == 'D':
        if i != N-1:
            if Map[i][j] == '.':
                Map[i][j] = '|'
            elif Map[i][j] == '-':
                Map[i][j] = '+'
            i += 1
            if Map[i][j] == '.':
                Map[i][j] = '|'
            elif Map[i][j] == '-':
                Map[i][j] = '+'
    elif cmd == 'L':
        if j:
            if Map[i][j] == '.':
                Map[i][j] = '-'
            elif Map[i][j] == '|':
                Map[i][j] = '+'
            j -= 1
            if Map[i][j] == '.':
                Map[i][j] = '-'
            elif Map[i][j] == '|':
                Map[i][j] = '+'
    else:
        if j != N-1:
            if Map[i][j] == '.':
                Map[i][j] = '-'
            elif Map[i][j] == '|':
                Map[i][j] = '+'
            j += 1
            if Map[i][j] == '.':
                Map[i][j] = '-'
            elif Map[i][j] == '|':
                Map[i][j] = '+'
for line in Map:
    print(*line, sep='')