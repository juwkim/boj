from collections import deque
import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
N, M = map(int, input().split())
Map = [g() for _ in range(N)]

cnt, Max = 0, 0
for i in range(N):
    for j in range(M):
        if Map[i][j]:
            cnt += 1
            area = 1
            Map[i][j] = 0
            dq = deque([(i, j)])
            while dq:
                x, y = dq.popleft()
                for p, q in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                    if 0 <= p < N and 0 <= q < M and Map[p][q]:
                        area += 1
                        Map[p][q] = 0
                        dq.append((p, q))
            Max = max(Max, area)
print(cnt)
print(Max)