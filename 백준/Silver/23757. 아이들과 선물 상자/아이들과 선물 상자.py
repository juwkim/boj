import heapq
g = lambda: [*map(int, input().split())]

N, M = g()
c = [-num for num in g()]
heapq.heapify(c)
ans = 1
for w in g():
    if c and -c[0] >= w:
        num = heapq.heappop(c) + w
        if num:
            heapq.heappush(c, num)
    else:
        ans = 0
        break
print(ans)