import sys
input = lambda: sys.stdin.readline().rstrip()

h, w = map(int, input().split())
a = [input() for _ in range(h)]
def solve():
    tot = sum(l.count('*') for l in a)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if a[i][j] == '*' and a[i - 1][j] == '*' and a[i + 1][j] == '*' and a[i][j - 1] == '*' and a[i][j + 1] == '*':
                tot -= 5
                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                    x, y = i + 2 * dx, j + 2 * dy
                    while 0 <= x < h and 0 <= y < w and a[x][y] == '*':
                        tot -= 1
                        x += dx
                        y += dy
                if tot == 0:
                    return "YES"
                return "NO"
    return "NO"
print(solve())