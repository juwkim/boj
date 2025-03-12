import sys
input = lambda: sys.stdin.readline().rstrip()

m, n = map(int, input().split())
a = [[*input()] for _ in range(m)]
for i in range(m):
    for j in range(n):
        if a[i][j] in 'ox':
            continue
        print(i + 1, j + 1)
        a[i][j] = 'o'
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            x, y = i + dx, j + dy
            while 0 <= x < m and 0 <= y < n and a[x][y] != 'x':
                a[x][y] = 'o'
                x, y = x + dx, y + dy