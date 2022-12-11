N, M = map(int, input().split())
Map = [[*input()] for _ in range(3 * N)]
for i in range(1, 3 * N, 3):
    for j in range(1 + 3 * (i & 1), 3 * M, 3):
        flag = False
        if i - 2 >= 0 and Map[i-2][j] == '#':
            Map[i-1][j] = '#'
            flag = True
        if i + 2 < 3 * N and Map[i+2][j] == '#':
            Map[i+1][j] = '#'
            flag = True
        if j - 2 >= 0 and Map[i][j-2] == '#':
            Map[i][j-1] = '#'
            flag = True
        if j + 2 < 3 * M and Map[i][j+2] == '#':
            Map[i][j+1] = '#'
            flag = True
        if flag:
            Map[i][j] = '#'
for line in Map:
    print(*line, sep='')