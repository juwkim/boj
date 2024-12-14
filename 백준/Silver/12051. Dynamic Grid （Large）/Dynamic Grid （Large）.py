import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

for tc in range(1, 1 + int(input())):
    R, C = map(int, input().split())
    a = [[*map(int, input())] for _ in range(R)]
    print(f'Case #{tc}:')
    for _ in range(int(input())):
        s = input()
        if s == 'Q':
            ans = 0
            visited = [bytearray(C) for _ in range(R)]
            for i in range(R):
                for j in range(C):
                    if a[i][j] and not visited[i][j]:
                        dq = deque([(i, j)])
                        visited[i][j] = 1
                        while dq:
                            x, y = dq.popleft()
                            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < R and 0 <= ny < C and a[nx][ny] and not visited[nx][ny]:
                                    visited[nx][ny] = 1
                                    dq.append((nx, ny))
                        ans += 1
            print(ans)
        else:
            x, y, z = map(int, s.split()[1:])
            a[x][y] = z