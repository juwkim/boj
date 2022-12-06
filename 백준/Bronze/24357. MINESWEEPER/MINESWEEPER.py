g = lambda: [*map(int, input().split())]

import sys
input = lambda: sys.stdin.readline().rstrip('\n')

margin = [[0, 0, 0, 0, 0]]
a = [[0] + g() + [0] for _ in range(3)]
a = margin + a + margin
for i in range(1, 4):
    for j in range(1, 4):
        if a[i][j] == 9:
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    a[x][y] = min(9, a[x][y] + 1)
for i in range(1, 4):
    print(*a[i][1:4])