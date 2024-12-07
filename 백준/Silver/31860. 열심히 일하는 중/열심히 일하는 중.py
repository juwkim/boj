import heapq

N, M, K = map(int, input().split())
hq = [-int(input()) for _ in range(N)]
heapq.heapify(hq)
ans = [0]
while hq:
    P = -heapq.heappop(hq)
    ans.append(ans[-1] // 2 + P)
    if P - M > K:
        heapq.heappush(hq, M - P)
print(len(ans) - 1)
print(*ans[1:], sep='\n')