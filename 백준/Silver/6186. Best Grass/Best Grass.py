R, C = map(int, input().split())
Map = [[*input()] + ['.'] for _ in range(R)] + [['.'] * (C + 2)]

cnt = 0
for i in range(R):
    for j in range(C):
        if Map[i][j] == '#':
            Map[i+1][j] = '.'
            Map[i][j+1] = '.'
            cnt += 1
print(cnt)