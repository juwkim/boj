g = lambda: map(int, input().split())

n, m, k = g()
ans = 0
for num in g():
    q, r = divmod(k, m)
    ans += q * (m // num) + r // num
print(ans)