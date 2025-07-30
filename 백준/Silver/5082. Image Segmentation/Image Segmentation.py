import sys
input = sys.stdin.readline
from collections import deque
g = lambda: list(map(int, input().split()))

while True:
    H, W, S, L = g()
    if H == 0:
        break
    banded = [[0] * W for _ in range(H)]
    for i in range(H):
        row = g()
        for j in range(W):
            R, G, B = row[3*j], row[3*j+1], row[3*j+2]
            rband = R // S
            gband = G // S
            bband = B // S
            banded[i][j] = (rband << 16) | (gband << 8) | bband
    visited = [bytearray(W) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if visited[i][j]:
                continue
            visited[i][j] = True
            color = banded[i][j]
            dq = deque([(i, j)])
            size = 0
            while dq:
                x, y = dq.popleft()
                size += 1
                for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and banded[nx][ny] == color:
                        visited[nx][ny] = True
                        dq.append((nx, ny))
            ans += size >= L
    print(ans)