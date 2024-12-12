import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

while True:
    W, H = map(int, input().split())
    if W == 0:
        break
    a = [[*input()] for _ in range(H)]
    visited = [bytearray(W) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if a[i][j] != 'S' or visited[i][j]:
                continue
            visited[i][j] = 1
            dq = deque([(i, j)])
            while dq:
                x, y = dq.popleft()
                for nx, ny in (x, y+1), (x, y-1), (x+1, y), (x-1, y):
                    if 0 <= nx < H and 0 <= ny < W and a[nx][ny] == 'T':
                        a[nx][ny] = 'S'
                        visited[nx][ny] = 1
                        dq.append((nx, ny))
    for l in a:
        print(*l, sep='')