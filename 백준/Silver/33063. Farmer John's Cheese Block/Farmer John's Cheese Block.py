import sys
g = lambda: map(int, sys.stdin.readline().split())

N, Q = g()
xy = [[0] * N for _ in range(N)]
yz = [[0] * N for _ in range(N)]
zx = [[0] * N for _ in range(N)]
ans = 0
for _ in range(Q):
    x, y, z = g()
    xy[x][y] += 1
    yz[y][z] += 1
    zx[z][x] += 1
    ans += (xy[x][y] == N) + (yz[y][z] == N) + (zx[z][x] == N)
    print(ans)