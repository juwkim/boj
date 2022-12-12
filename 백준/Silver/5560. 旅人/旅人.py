g = lambda: map(int, input().split())

mod = 10 ** 5
n, m = g()
px = [0]
for _ in range(n - 1):
    px.append(px[-1] + int(input()))
ans, cur = 0, 0
for i in range(m):
    Next = cur + int(input())
    ans = (ans + abs(px[cur] - px[Next])) % mod
    cur = Next
print(ans)