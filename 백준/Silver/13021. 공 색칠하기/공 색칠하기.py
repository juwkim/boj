import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
colors, num = [0] * N, 1
for _ in range(M):
    L, R = g()
    for i in range(L - 1, R): colors[i] = num
    num <<= 1
print(1 << len({*colors} - {0}))