import heapq

n, k = map(int, input().split())
q = [(val, val, 1) for val in {*map(int, input().split())}]
heapq.heapify(q)
prev, ans = 0, 0
while q[0][0] <= n:
    cur, base, mul = q[0]
    heapq.heappushpop(q, (base * (mul + 1), base, mul + 1))
    ans += max(0, cur - prev - 1)
    prev = cur
ans += n - prev
print(ans)