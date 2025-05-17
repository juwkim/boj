n = int(input())
ans, i = 0, 2
while i <= n:
    e = min(n - i, i - 1)
    ans += e * (e + 1)
    i <<= 1
ans >>= 1
print(ans)