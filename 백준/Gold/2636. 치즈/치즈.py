import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from copy import deepcopy
from collections import deque

r, c = g()
cheese = [g() for _ in range(r)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

cheese[0][0] = 2
def mark_edge(): # 0: hole, 1: cheese, 2: edge
    dq = deque([(0, 0)])
    visited = [[False] * c for _ in range(r)]
    visited[0][0] = True
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and cheese[nx][ny] in (0, 2):
                visited[nx][ny] = True
                cheese[nx][ny] = 2
                dq.append((nx, ny))

def melt():
    global cheese
    melted = 0
    new_cheese = deepcopy(cheese)
    for x in range(r):
        for y in range(c):
            if cheese[x][y] != 1:
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and cheese[nx][ny] == 2:
                    melted += 1
                    new_cheese[x][y] = 2
                    break
    cheese = new_cheese
    return melted

time = 0
while True:
    time += 1
    mark_edge()
    melted = melt()
    if all(all(num != 1 for num in line) for line in cheese):
        break
print(time)
print(melted)