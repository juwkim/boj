import sys
input = sys.stdin.readline

R, C = map(int, input().split())
a = [input() for _ in range(R)]
red = [[0] * C for _ in range(R)]
blue = [[0] * C for _ in range(R)]
if a[0][0] == 'R':
    red[0][0] = 1
else:
    blue[0][0] = 1
for i in range(R):
    for j in range(C):
        if a[i][j] == 'R':
            for x in range(i + 1, R):
                for y in range(j + 1, C):
                    if a[x][y] == 'B':
                        blue[x][y] += red[i][j]
        else:
            for x in range(i + 1, R):
                for y in range(j + 1, C):
                    if a[x][y] == 'R':
                        red[x][y] += blue[i][j]
print(red[-1][-1] if red[-1][-1] else blue[-1][-1])