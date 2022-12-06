import sys
input = lambda: sys.stdin.readline().rstrip('\n')

g = lambda: [*map(int, input().split())]

M, N = g()
U, L, R, D = g()
l = N + L + R
a = (l + 2) // 2 * '#.'
Map = [[*a[_%2:_%2+l]] for _ in range(M + U + D)]

for i in range(U, U+M):
    Map[i][L:L+N] = input()
for line in Map:
    print(*line, sep='')