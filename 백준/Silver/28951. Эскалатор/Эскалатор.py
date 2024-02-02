n = int(input())
ans = n != 1
if n % 10:
    ans += len(str(n))
t = 2
while n >= 10 ** t:
    ans += 9 * t * 10 ** (t - 2)
    t += 1
n -= n % 10
ans += ((n - 10 ** (t - 1)) // 10 + 1) * t
print(ans)