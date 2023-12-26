import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

H, W, X, Y = g()
B = [g() for _ in range(H + X)]
A = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i < X or j < Y:
            A[i][j] = B[i][j]
        else:
            A[i][j] = B[i][j] - A[i - X][j - Y]
for row in A:
    print(*row)