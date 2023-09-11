import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

Y, X = g()
poster = [list(input()) for _ in range(Y)]
buf = [['B'] * X for _ in range(Y)]
ans = "NO"
if X & 1:
    j = X // 2
    for i in range(Y):
        if all(poster[i][k] == 'X' for k in range(j - 1, j + 2)):
            ans = "YES"
            break
    if ans == "YES":
        buf[i][j - 1] = 'W'
        buf[i][j] = 'Y'
        buf[i][j + 1] = 'W'
else:
    j1, j2 = X // 2 - 1, X // 2
    for i in range(Y):
        if all(poster[i][k] == 'X' for k in range(j1 - 1, j2 + 2)):
            ans = "YES"
            break
    if ans == "YES":
        buf[i][j1 - 1] = 'W'
        buf[i][j1] = 'Y'
        buf[i][j2] = 'Y'
        buf[i][j2 + 1] = 'W'
if ans == "NO":
    print("NO")
else:
    print("YES")
    for line in buf:
        print(*line, sep='')