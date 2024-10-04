import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

for _ in range(int(input())):
    w, h = map(int, input().split())
    fire, player = deque(), deque()
    visited = [bytearray(w) for _ in range(h)]
    for i in range(h):
        for j, c in enumerate(input()):
            if c != '.':
                visited[i][j] = 1
            if c == '*':
                fire.append((i, j))
            elif c == '@':
                player.append((i, j))
    ans, time = 'IMPOSSIBLE', 0
    while player:
        time += 1
        for _ in range(len(fire)):
            x, y = fire.popleft()
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    fire.append((nx, ny))
        for _ in range(len(player)):
            x, y = player.popleft()
            if x == 0 or x == h - 1 or y == 0 or y == w - 1:
                ans = time
                break
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    player.append((nx, ny))
        if ans != 'IMPOSSIBLE':
            break
    print(ans)