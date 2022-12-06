from itertools import chain
X, Y, I = map(int, input().split())
field = [[0] * Y for _ in range(X)]
for _ in range(I):
    XII, YII, Xur, Yur = map(int, input().split())
    for x in range(XII-1, Xur):
        for y in range(YII-1, Yur):
            field[x][y] = 1
print(sum(chain(*field)))