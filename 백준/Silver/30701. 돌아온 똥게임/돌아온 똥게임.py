import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, D = g()
buf = [[], []]
for _ in range(N):
    A, X = g()
    buf[A - 1].append(X)
buf[0].sort()
buf[1].sort()
i, j = 0, 0
while True:
    while i < len(buf[0]) and buf[0][i] < D:
        D += buf[0][i]
        i += 1
    if i == len(buf[0]) or j == len(buf[1]):
        j = len(buf[1])
        break
    D *= buf[1][j]
    j += 1
print(i + j)