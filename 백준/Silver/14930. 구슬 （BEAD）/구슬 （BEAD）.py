import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, t = g()
beads = [g() for _ in range(N)]
rank = sum(beads[0][0] > beads[i][0] for i in range(1, N))
print(sorted(x + t * v for x, v in beads)[rank])