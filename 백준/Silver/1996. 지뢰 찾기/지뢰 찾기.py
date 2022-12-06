N = int(input())
field = [input() for _ in range(N)]

Map = [[0 for _ in range(N+2)] for _ in range(N+2)]

for i in range(N):
    for j in range(N):
        if field[i][j] != '.':
            s = int(field[i][j])
            for k in range(3):
                Map[i][j+k] += s
                Map[i+2][j+k] += s
            Map[i+1][j] += s
            Map[i+1][j+2] += s

for i in range(N):
    for j in range(N):
        if field[i][j] != '.':
            Map[i+1][j+1] = '*'
            

for i in range(1, N+1):
    for j in range(1, N+1):
        s = Map[i][j]
        print(s if s == '*' or s < 10 else 'M', end='')
    print()
