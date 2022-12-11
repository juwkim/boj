g = lambda: map(int, input().split())
a, b, c, d = g()
ans = 0
for _ in range(int(input())):
    u, v = g()
    ans += a * (v - b) ** 2 == u - c
print(ans)