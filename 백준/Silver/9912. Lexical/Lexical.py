n, *nums = map(int, open(0).read().split())
f, d = 1, n
for i in range(2, n + 1): f *= i
s = {*range(n)}
ans = 0
for num in nums:
    f //= d
    d -= 1
    cnt = sum(a < num for a in s)
    ans += cnt * f
    s.remove(num)
print(ans + 1)