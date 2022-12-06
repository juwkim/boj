import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

hq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(hq, x)
    else:
        print(heapq.heappop(hq) if hq else 0)