import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, Q = g()
px = [[0], [0], [0]]
for _ in range(N):
    num = int(input())
    px[0].append(px[0][-1] + (num == 1))
    px[1].append(px[1][-1] + (num == 2))
    px[2].append(px[2][-1] + (num == 3))
for _ in range(Q):
    a, b = g()
    print(px[0][b] - px[0][a - 1], px[1][b] - px[1][a - 1], px[2][b] - px[2][a - 1])