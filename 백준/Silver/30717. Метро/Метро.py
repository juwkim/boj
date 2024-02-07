g = lambda: map(int, input().split())

n, p, k = g()
ans = 0
for r, num in sorted((k - num % k, num) for num in g()):
    if p >= r:
        p -= r
        num += r
    ans += num // k
ans += p // k
print(ans)