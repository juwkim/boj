g = lambda: map(int, input().split())
R, C = g()
Map = [list(input()) for _ in range(R)]
def check():
    for i in range(R):
        for j in range(C):
            if Map[i][j] == 'S':
                for s, t in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= s < R and 0 <= t < C:
                        if Map[s][t] == 'W':
                            return 0
                        if Map[s][t] == '.':
                            Map[s][t] = 'D'
    return 1

if check():
    print(1)
    for line in Map:
        print(*line, sep='')
else:
    print(0)