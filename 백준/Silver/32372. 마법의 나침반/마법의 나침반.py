import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
xmin, xmax = 1, N
ymin, ymax = 1, N
for _ in range(M):
    X, Y, K = g()
    match K:
        case 1 | 2 | 8:
            xmax = min(xmax, X - 1)
        case 4 | 5 | 6:
            xmin = max(xmin, X + 1)
        case _:
            xmin = xmax = X
    match K:
        case 6 | 7 | 8:
            ymax = min(ymax, Y - 1)
        case 2 | 3 | 4:
            ymin = max(ymin, Y + 1)
        case _:
            ymin = ymax = Y
print(xmin, ymin)