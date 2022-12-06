from collections import deque
import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N, M = g()
Map = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def bfs(x, y):
    val = 1
    dq = deque([(x, y, val)])
    visited[x][y] = 1
    while dq:
        x, y, val = dq.popleft()
        if x == N-1 and y == M-1:
            print(val)
            return
        for Next in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            x, y = Next
            if x < 0 or x >= N or y < 0 or y >= M or Map[x][y] == '0' or visited[x][y]:
                continue
            visited[x][y] = 1
            dq.append((x, y, val+1))
bfs(0, 0)