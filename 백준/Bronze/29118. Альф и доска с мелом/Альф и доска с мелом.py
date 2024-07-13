n, k = map(int, input().split())

if k == 0 or n % 10 == 0:
    ans = n
elif n % 10 == 5:
    ans = n + 5
else:
    if n & 1:
        n += n % 10
        k -= 1
    q, r = divmod(k, 4)
    ans = n + q * 20
    for _ in range(r):
        ans += ans % 10
print(ans)