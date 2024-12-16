import heapq

n, *a = map(int, open(0).read().split())
hq = [(-num, i) for i, num in enumerate(a, 1) if num]
heapq.heapify(hq)
ans = []
while len(hq) > 1:
    num1, i = heapq.heappop(hq)
    num2, j = heapq.heappop(hq)
    if num1 + 1: heapq.heappush(hq, (num1 + 1, i))
    if num2 + 1: heapq.heappush(hq, (num2 + 1, j))
    ans.append((i, j))
if hq:
    print("no")
else:
    print("yes")
    for a, b in ans:
        print(a, b)