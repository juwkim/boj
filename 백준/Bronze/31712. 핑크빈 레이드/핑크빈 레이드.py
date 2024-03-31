import heapq

hq = [[0, *map(int, input().split())] for _ in range(3)]
heapq.heapify(hq)
H = int(input())
t = 0
while H > 0:
    t, C, D = heapq.heappop(hq)
    H -= D
    heapq.heappush(hq, [t + C, C, D])
print(t)