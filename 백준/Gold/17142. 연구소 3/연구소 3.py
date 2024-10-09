import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from itertools import combinations
from collections import deque

def solve():
    N, M = g()
    A = [g() for _ in range(N)]
    zero = sum(r.count(0) for r in A)
    if zero == 0:
        return 0
    virus = [(i, j, 1) for i in range(N) for j in range(N) if A[i][j] == 2]
    ans = 1e9
    for l in combinations(virus, M):
        dq = deque(l)
        visited = [bytearray(N) for _ in range(N)]
        for x, y, _ in l:
            visited[x][y] = 1
        cur_zero = 0
        while dq and cur_zero < zero:
            x, y, cnt = dq.popleft()
            for nx, ny in (x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y):
                if 0 <= nx < N and 0 <= ny < N and A[nx][ny] != 1 and not visited[nx][ny]:
                    if A[nx][ny] == 0:
                        cur_zero += 1
                    visited[nx][ny] = 1
                    dq.append((nx, ny, cnt + 1))
        if cur_zero == zero:
            ans = min(ans, cnt)
    if ans == 1e9:
        return -1
    return ans

print(solve())