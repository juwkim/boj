g = lambda: [*map(int, input().split())]


n, m = g()
Map = [[*input()] for _ in range(n)]
for i in range(n-2, -1, -1):
    for j in range(m-2, -1, -1):
        if Map[i][j] == '#':
            Map[i+1][j] = '#'
            Map[i][j+1] = '#'
            Map[i+1][j+1] = '#'
for line in Map:
    print(*line, sep='')