import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
buf = [list(input()) for _ in range(3 * N)]
for i in range(1, 3 * N, 3):
    for j in range(1, 8 * M, 8):
        p = 5 + (buf[i][j+5] != '.')
        problem = buf[i][j:j+p]
        if eval("".join(problem).replace('=', '==')):
            buf[i-1][j:j+p] = ['*'] * p
            buf[i+1][j:j+p] = ['*'] * p
            buf[i][j-1] = '*'
            buf[i][j+p] = '*'
        else:
            buf[i-1][j+2] = '/'
            buf[i][j+1] = '/'
            buf[i+1][j] = '/'
for l in buf:
    print(*l, sep='')