import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def find():
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if A[i][j][k] == 'S':
                    return i, j, k
while (nums:=[*map(int, input().split())])[0]:
    L, R, C = nums
    A = [[input() for _ in range(R + 1)] for _ in range(L)]
    x, y, z = find()
    dq = deque([(x, y, z, 1)])
    visited = [[bytearray(C) for _ in range(R)] for _ in range(L)]
    visited[x][y][z] = 1
    ans = "Trapped!"
    while dq:
        x, y, z, cnt = dq.popleft()
        for dx, dy, dz in ((0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)):
            nx, ny, nz = x + dx, y + dy, z + dz
            if nx < 0 or ny < 0 or nz < 0 or nx >= L or ny >= R or nz >= C or visited[nx][ny][nz] or A[nx][ny][nz] == '#':
                continue
            if A[nx][ny][nz] == 'E':
                ans = f"Escaped in {cnt} minute(s)."
                break
            dq.append((nx, ny, nz, cnt + 1))
            visited[nx][ny][nz] = 1
        else:
            continue
        break
    print(ans)