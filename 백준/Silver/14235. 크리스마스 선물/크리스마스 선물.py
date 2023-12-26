import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

import heapq

qu = []
for _ in range(int(input())):
    a, *nums = g()
    if a == 0:
        if not qu:
            print(-1)
        else:
            print(-heapq.heappop(qu))
    else:
        for num in nums:
            heapq.heappush(qu, -num)