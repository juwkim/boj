import heapq

N, centi, T = map(int, input().split())
H = [-int(input()) for _ in range(N)]
heapq.heapify(H)
ans = T
for i in range(T):
    num = -H[0]
    if num < centi or num == 1:
        ans = i
        break
    num = -heapq.heappop(H)
    heapq.heappush(H, -(num // 2))
num = -heapq.heappop(H)
if num < centi:
    print("YES")
    print(ans)
else:
    print("NO")
    print(num)