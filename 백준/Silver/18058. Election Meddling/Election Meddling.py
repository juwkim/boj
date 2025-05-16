import sys
import heapq
g = lambda: map(int, sys.stdin.readline().split())

w, p = g()
target = (w >> 1) + 1
bribes = []
for _ in range(w):
    icpc, *others = g()
    hq = [-other for other in others if other]
    heapq.heapify(hq)
    if not hq or icpc > -hq[0]:
        target -= 1
    else:
        cnt = 0
        while hq and icpc <= -hq[0]:
            cnt += 1
            icpc += 1
            prv = heapq.heappop(hq) + 1
            if prv:
                heapq.heappush(hq, prv)
        bribes.append(cnt)
if target > 0:
    ans = sum(sorted(bribes)[:target])
else:
    ans = 0
print(ans)