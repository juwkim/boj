import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, L = g()
pos, time = 0, 0
for x, g, r in sorted(g() for _ in range(N)):
    time += x - pos
    pos = x
    q = time % (g + r)
    if q >= g:
        time += g + r - q
time += L - pos
print(time)