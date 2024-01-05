import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

import heapq

N, M = g()
Out = [[] for _ in range(N + 1)]
In = [0 for _ in range(N + 1)]
for _ in range(M):
    A, B = g()
    Out[A].append(B)
    In[B] += 1

ans = []
heap = [i for i in range(1, N + 1) if In[i] == 0]
heapq.heapify(heap)
while heap:
    num = heapq.heappop(heap)
    ans.append(num)
    for nxt in Out[num]:
        In[nxt] -= 1
        if In[nxt] == 0:
            heapq.heappush(heap, nxt)
print(*ans)