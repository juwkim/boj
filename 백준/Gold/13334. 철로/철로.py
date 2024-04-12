import sys
input = sys.stdin.readline
import heapq

n = int(input())
nums = sorted([sorted(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
d = int(input())
ans = 0
hq = []
for h, o in nums:
    while hq and o - hq[0][0] > d:
        heapq.heappop(hq)
    s = min(h, hq[0][0]) if hq else h
    if o - s <= d:
        heapq.heappush(hq, (h, o))
        ans = max(ans, len(hq))
print(ans)