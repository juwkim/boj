import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
icebergs = [g() for _ in range(N)]
ans = 0
while True:
    ans += 1
    visited = [[False] * M for _ in range(N)]
    melted = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if icebergs[i][j] == 0:
                continue
            melt = 0
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M and icebergs[nx][ny] == 0:
                    melt += 1
            melted[i][j] = melt
    for i in range(N):
        for j in range(M):
            icebergs[i][j] = max(icebergs[i][j] - melted[i][j], 0)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if icebergs[i][j] and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M and icebergs[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
    if cnt >= 2:
        break
    if cnt == 0:
        ans = 0
        break
print(ans)