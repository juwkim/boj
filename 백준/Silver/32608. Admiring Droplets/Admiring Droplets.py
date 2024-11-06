import sys
g = lambda: map(int, sys.stdin.readline().split())

n, h = g()
time = 0
scur, ycur = g()
p = 10 ** 1.5
for _ in range(n - 1):
    s, y = g()
    time += (y - ycur) / (p * scur ** (1 / 6))
    ycur = y
    scur += s
time += (h - ycur) / (p * scur ** (1 / 6))
print(time)