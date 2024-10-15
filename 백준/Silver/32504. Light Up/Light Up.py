import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = [' ' * (n + 2)] + [[*' ' + input() + ' '] for _ in range(n)] + [' ' * (n + 2)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i][j].isdigit():
                if int(a[i][j]) != sum(a[x][y] == '?' for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))):
                    return 0
            elif a[i][j] == '?':
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    while a[ni][nj] in ".!":
                        a[ni][nj] = '!'
                        ni += di
                        nj += dj
                    if a[ni][nj] == '?':
                        return 0
    if any(any(c == '.' for c in row) for row in a):
        return 0
    return 1

print(solve())