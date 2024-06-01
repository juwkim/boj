import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import product

for _ in range(int(input())):
    m, n = map(int, input().split())
    b = [input().lower() for _ in range(m)]
    for _ in range(int(input())):
        s = input().lower()
        l = len(s)
        def solve():
            for i in range(m):
                for j in range(n):
                    for dx, dy in product((-1, 0, 1), repeat=2):
                        if (dx, dy) == (0, 0):
                            continue
                        ex, ey = i + (l - 1) * dx, j + (l - 1) * dy
                        if ex < 0 or ex >= m or ey < 0 or ey >= n:
                            continue
                        if all(b[i + k * dx][j + k * dy] == s[k] for k in range(l)):
                            return i + 1, j + 1
            return m, n
        print(*solve())
    print()