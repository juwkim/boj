import heapq

n, s, m, *t = map(int, open(0).read().split())
hq = [(0, i, num) for i, num in enumerate(t)]
heapq.heapify(hq)
for _ in range(n - s):
    time, num, speed = heapq.heappop(hq)
    heapq.heappush(hq, (time + speed, num, speed))
print(num + 1)