import heapq

N, K, *P = map(int, open(0).read().split())
hq = [(-num, i) for i, num in enumerate(P) if num > 100]
heapq.heapify(hq)
while hq and K:
    num, i = heapq.heappop(hq)
    P[i] -= 100
    if num < -200:
        heapq.heappush(hq, (num + 100, i))
    K -= 1
if K:
    print("impossible")
else:
    print(*P)