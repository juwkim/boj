n = int(input())
s = len(str(n))
ans = n != 1
if n % 10:
    ans += s
ans += s * 10 ** (s - 2) - (10 ** (s - 1) + 8) // 9 if s > 1 else 0
n -= n % 10
ans += ((n - 10 ** (s - 1)) // 10 + 1) * s
print(ans)