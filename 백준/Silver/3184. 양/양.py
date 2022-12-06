import sys
sys.setrecursionlimit(10**5)
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]

R, C = g()
Map = [input() for _ in range(R)]
visited = [bytearray(C) for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

v, k = 0, 0
buf = [0, 0]
def dfs(x, y):
    visited[x][y] = 1
    if Map[x][y] == 'v':
        buf[0] += 1
    elif Map[x][y] == 'o':
        buf[1] += 1
    elif Map[x][y] == '#':
        return

    for a, b in zip(dx, dy):
        i, j = x + a, y + b
        if 0 <= i < R and 0 <= j < C and visited[i][j] == 0:
            dfs(i, j)

for x in range(R):
    for y in range(C):
        if Map[x][y] in '#':
            visited[x][y] = 1
        elif Map[x][y] == '.':
            continue
        elif visited[x][y] == 0:
            dfs(x, y)
            a, b = buf
            if a < b:
                a = 0
            else:
                b = 0
            v += a
            k += b
            buf = [0, 0]
print(k, v)