import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

import heapq

N = int(input())
room = []
for s, t in sorted(g() for _ in range(N)):
    if room and room[0] <= s:
        heapq.heappop(room)
    heapq.heappush(room, t)
print(len(room))