import heapq

n, m, *a = map(int, open(0).read().split())
hq = [0] * m
ans = 0
for num in sorted(a):
    t = heapq.heappop(hq)
    ans += t + num
    heapq.heappush(hq, t + num)
print(ans)