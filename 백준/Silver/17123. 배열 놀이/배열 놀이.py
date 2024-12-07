import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N, M = g()
    A = [g() for _ in range(N)]
    row, col = [sum(l) for l in A], [sum(l) for l in zip(*A)]
    for _ in range(M):
        r1, c1, r2, c2, v = g()
        for i in range(r1 - 1, r2):
            row[i] += (c2 - c1 + 1) * v
        for i in range(c1 - 1, c2):
            col[i] += (r2 - r1 + 1) * v
    print(*row)
    print(*col)