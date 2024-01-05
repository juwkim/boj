import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

mod = 1_000_000_007
D = int(input())
matrix = {
    1: [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0]
    ]
}

def matrix_mul(a, b):
    n = 8
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= mod
    return c

def solve(n):
    if n in matrix:
        return matrix[n]
    if n % 2 == 0:
        matrix[n] = matrix_mul(solve(n // 2), solve(n // 2))
    else:
        matrix[n] = matrix_mul(solve(n - 1), solve(1))
    return matrix[n]

ans = solve(D)[0][0]
print(ans)