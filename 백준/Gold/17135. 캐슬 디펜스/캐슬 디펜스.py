import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from itertools import combinations
from collections import deque

def bfs(x, y):
    dq = deque([(x, y)])
    visited = [bytearray(M) for _ in range(N + 1)]
    visited[x][y] = 1
    while dq:
        i, j = dq.popleft()
        if B[i][j]:
            return i, j
        for ni, nj in (i, j - 1), (i - 1, j), (i, j + 1):
            if ni >= 0 and 0 <= nj < M and not visited[ni][nj] and abs(ni - x) + abs(nj - y) <= D:
                dq.append((ni, nj))
                visited[ni][nj] = 1
    return -1, -1

N, M, D = g()
A = [g() for _ in range(N)] + [[0] * M]
ans = 0
for a, b, c in combinations(range(M), 3):
    B, cur = [r[:] for r in A], 0
    while any(any(r) for r in B):
        p1, q1 = bfs(N, a)
        p2, q2 = bfs(N, b)
        p3, q3 = bfs(N, c)
        if B[p1][q1]:
            B[p1][q1] = 0
            cur += 1
        if B[p2][q2]:
            B[p2][q2] = 0
            cur += 1
        if B[p3][q3]:
            B[p3][q3] = 0
            cur += 1
        B = [[0] * M] + B[:-2] + [[0] * M]
    ans = max(ans, cur)
print(ans)