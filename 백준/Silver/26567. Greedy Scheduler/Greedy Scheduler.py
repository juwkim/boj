import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
import heapq

for _ in range(int(input())):
    n, c = g()
    hq = [(0, i) for i in range(1, n + 1)]
    heapq.heapify(hq)
    ans = []
    for t in g():
        d, i = heapq.heappop(hq)
        ans.append(i)
        heapq.heappush(hq, (d + t, i))
    print(*ans)