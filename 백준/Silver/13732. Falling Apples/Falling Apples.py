N, M = map(int, input().split())
Map = [[*input()] for _ in range(N)]
for j in range(M):
    pos = N - 1
    for i in range(N - 1, -1, -1):
        if Map[i][j] == '#':
            pos = i - 1
        elif Map[i][j] == 'a':
            Map[i][j] = '.'
            Map[pos][j] = 'a'
            pos -= 1
            while Map[pos][j] == '#':
                pos -= 1
for line in Map:
    print(''.join(line))