import sys
from collections import deque
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for tc in range(1, int(input()) + 1):
    R, C = g()
    A, B = map(lambda x: int(x) - 1, input().split())
    grid = [g() for _ in range(R)]
    visited = [bytearray(C) for _ in range(R)]
    visited[A][B] = True
    dq = deque([(A, B)])
    ans = 0
    while dq:
        r, c = dq.popleft()
        ans += r == 0 or r == R - 1 or c == 0 or c == C - 1
        for nr, nc in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] >= grid[r][c]:
                visited[nr][nc] = True
                dq.append((nr, nc))
    print(f"Case #{tc}: {ans}")