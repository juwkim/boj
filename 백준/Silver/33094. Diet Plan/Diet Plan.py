import heapq

N, M, K, *P = map(int, open(0).read().split())
hq = [P[i] for i in range(min(N, K))]
heapq.heapify(hq)
ans = N
for i in range(K, N):
    num = P[i]
    if hq and num > hq[0]:
        M -= heapq.heappop(hq)
        heapq.heappush(hq, num)
    else:
        M -= num
    if M < 0:
        ans = i
        break
print(ans)