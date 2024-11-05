import sys
input = sys.stdin.readline
from collections import defaultdict
import heapq

d = defaultdict(list)
for _ in range(int(input())):
    a, b = input().split()
    d[a].append(b)
hq = [(-len(v), k) for k, v in d.items()]
prev = None
while hq:
    l1, k1 = heapq.heappop(hq)
    if prev != k1:
        print(d[k1].pop())
        if l1 + 1:
            heapq.heappush(hq, (l1 + 1, k1))
        prev = k1
    else:
        l2, k2 = heapq.heappop(hq)
        print(d[k2].pop())
        heapq.heappush(hq, (l1, k1))
        if l2 + 1:
            heapq.heappush(hq, (l2 + 1, k2))
        prev = k2