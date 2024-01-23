import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

R, S = g()
a = ["." * (S + 2)] + ["." + input() + "." for _ in range(R)] + ["." * (S + 2)]
ans = 0
good = 0
for i in range(1, R + 1):
    for j in range(1, S + 1):
        if a[i][j] == 'o':
            ans += a[i][j + 1] == 'o'
            ans += a[i + 1][j - 1] == 'o'
            ans += a[i + 1][j] == 'o'
            ans += a[i + 1][j + 1] == 'o'
        else:
            cur = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    cur += a[x][y] == 'o'
            good = max(good, cur)
print(ans + good)