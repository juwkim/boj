import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
d = g()
a, b = [0] * n, [0] * n
for i in range(n - 1):
    if d[i] in (1, 2):
        a[i + 1] = a[i] + 1
for i in range(n - 2, -1, -1):
    if d[i] in (0, 2):
        b[i] = b[i + 1] + 1
for i in range(n):
    print(a[i] + b[i], end=' ')