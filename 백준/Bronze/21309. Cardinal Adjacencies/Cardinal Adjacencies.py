import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]

r, c = g()
a = [[0] + g() + [0] for _ in range(r)] + [[0] * (c + 2)]

s, t = 0, 0
for i in range(r):
    for j in range(1, c + 1):
        s += (a[i][j] + a[i][j+1] == 2)
        s += (a[i][j] + a[i+1][j] == 2)
        t += (a[i][j] + a[i+1][j+1] == 2)
        t += (a[i][j] + a[i+1][j-1] == 2)
print(s, s + t)