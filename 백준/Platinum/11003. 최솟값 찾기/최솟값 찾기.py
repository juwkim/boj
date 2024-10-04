import heapq

N, L, *A = map(int, open(0).read().split())
hq = []
for i in range(N):
    if i >= L:
        while hq and hq[0][1] <= i - L:
            heapq.heappop(hq)
    heapq.heappush(hq, (A[i], i))
    print(hq[0][0], end=' ')