g = lambda: [*map(int, input().split())]
import heapq
K, N = g()
hq = [-num for num in g()]
heapq.heapify(hq)
cnt = 0
while True:
    num = heapq.heappop(hq)
    if num < -10:
        N -= 10
        heapq.heappush(hq, num+10)
    else:
        N += num
    cnt += 1
    if N <= 0:
        break
print(cnt)