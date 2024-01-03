import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]
from collections import deque, defaultdict

def bfs(x, y):
    cnt = 0
    dq = deque([(x, y)])
    visited[x][y] = 1
    while dq:
        x, y = dq.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if Map[nx][ny] == '*' or visited[nx][ny]:
                continue
            if Map[nx][ny].isupper() and Map[nx][ny] not in key:
                door[Map[nx][ny]].append((nx, ny))
                continue
            if Map[nx][ny] == '$':
                cnt += 1
            elif Map[nx][ny].islower():
                key.add(Map[nx][ny].upper())
            visited[nx][ny] = 1
            dq.append((nx, ny))
    return cnt

for _ in range(int(input())):
    h, w = g()
    Map = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    door = defaultdict(deque)
    key = set(map(str.upper, input()))
    key.discard('0')
    ans = 0
    for i in range(h):
        for j in range(w):
            if i not in (0, h - 1) and j not in (0, w - 1):
                continue
            if Map[i][j] == '*' or visited[i][j]:
                continue
            if Map[i][j].isupper() and Map[i][j] not in key:
                door[Map[i][j]].append((i, j))
                continue
            if Map[i][j] == '$':
                ans += 1
            elif Map[i][j].islower():
                key.add(Map[i][j].upper())
            ans += bfs(i, j)
    while True:
        flag = False
        for k in list(key):
            while door[k]:
                x, y = door[k].popleft()
                ans += bfs(x, y)
                flag = True
        if not flag:
            break
    print(ans)