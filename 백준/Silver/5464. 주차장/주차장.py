import sys
input = sys.stdin.readline
from collections import deque
import heapq

N, M = map(int, input().split())
cost = [0] + [int(input()) for _ in range(N)]
weight = [0] + [int(input()) for _ in range(M)]

ans, pos = 0, [0] * (M + 1)
dq, hq = deque(), [*range(1, N + 1)]
heapq.heapify(hq)
for _ in range(2 * M):
    num = int(input())
    if num < 0:
        heapq.heappush(hq, pos[-num])
        if not dq:
            continue
        num = dq.popleft()
    if hq:
        p = heapq.heappop(hq)
        ans += cost[p] * weight[num]
        pos[num] = p
    else:
        dq.append(num)
print(ans)