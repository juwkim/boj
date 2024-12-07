import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N, M = g()
A = [g() for _ in range(N)]
ans = []
for i in range(N):
    visited = [bytearray(M) for _ in range(N)]
    visited[i][0] = 1
    x, y = i, 0
    while True:
        y += A[x][y]
        if y >= M:
            break
        x += A[x][y]
        if x >= N:
            break
        y -= A[x][y]
        if y < 0:
            break
        x -= A[x][y]
        if x < 0:
            break
        if visited[x][y]:
            ans.append(i + 1)
            break
        visited[x][y] = 1
print(len(ans))
print(*ans)