from collections import deque

A = [[c for c in input()] for _ in range(12)]
ans = 0
while True:
    puyo = []
    for c in "RGBPY":
        visited = [[False]*6 for _ in range(12)]
        for i in range(12):
            for j in range(6):
                if A[i][j] == c and not visited[i][j]:
                    visited[i][j] = True
                    q = deque([(i,j)])
                    tmp = [(i,j)]
                    while q:
                        x, y = q.popleft()
                        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                            nx, ny = x+dx, y+dy
                            if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny] and A[nx][ny] == c:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                                tmp.append((nx,ny))
                    if len(tmp) >= 4:
                        puyo.extend(tmp)
    if not puyo:
        break
    ans += 1
    for x, y in puyo:
        A[x][y] = "."
    for j in range(6):
        tmp = []
        for i in range(12):
            if A[i][j] != ".":
                tmp.append(A[i][j])
        for i in range(12-len(tmp)):
            A[i][j] = "."
        for i in range(12-len(tmp), 12):
            A[i][j] = tmp[i-(12-len(tmp))]
print(ans)