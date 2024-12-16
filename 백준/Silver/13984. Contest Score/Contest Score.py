import heapq

n, k, *t = map(int, open(0).read().split())
ans, tot = 0, 0
hq = t[:k]
heapq.heapify(hq)
for i in range(k, n):
    tot += heapq.heapreplace(hq, t[i])
    ans += tot
while hq:
    tot += heapq.heappop(hq)
    ans += tot
print(ans)