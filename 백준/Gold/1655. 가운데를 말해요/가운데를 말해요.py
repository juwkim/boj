import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

import heapq

N = int(input())
l, r = [-int(input())], []
print(-l[0])
for _ in range(N - 1):
    num = int(input())
    if num >= -l[0]:
        heapq.heappush(r, num)
    else:
        heapq.heappush(l, -num)
    if len(l) < len(r):
        heapq.heappush(l, -heapq.heappop(r))
    elif len(l) > len(r) + 1:
        heapq.heappush(r, -heapq.heappop(l))
    print(-l[0])