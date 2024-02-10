n = int(input())
ans = (n - 1) // 2 * n
if n % 3 == 0:
    ans -= 2 * n // 3
print(ans)