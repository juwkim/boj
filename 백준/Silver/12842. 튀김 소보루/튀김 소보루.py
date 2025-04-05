import heapq

n, s, m, *t = map(int, open(0).read().split())
hq = [(0, i, speed) for i, speed in enumerate(t, 1)]
heapq.heapify(hq)
for _ in range(n - s):
    time, i, speed = heapq.heappop(hq)
    heapq.heappush(hq, (time + speed, i, speed))
print(i)