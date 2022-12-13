g = lambda: [*map(int, input().split())]

N, M = g()
Map = [[*input()] for _ in range(N)]
for k in range(N-1):
    for j in range(M):
        for i in range(N - 1):
            if (Map[i][j], Map[i + 1][j]) == ('o', '.'):
                 Map[i][j], Map[i + 1][j] = '.', 'o'
for line in Map:
    print(''.join(line))