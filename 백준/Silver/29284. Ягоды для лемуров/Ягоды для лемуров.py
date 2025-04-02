import heapq

input()
hq = []
ans = 0
for i, num in enumerate(map(int, input().split())):
    while hq and hq[0] <= i:
        heapq.heappop(hq)
    ans += num * len(hq)
    heapq.heappush(hq, i + num)
print(ans)