import heapq

n, k, *d = map(int, open(0).read().split())
d.sort()
hq = d[:k]
ans = sum(hq)
for i in range(k, n):
    num = d[i] + heapq.heappop(hq)
    ans += num
    heapq.heappush(hq, num)
print(ans)