m, n = int(input()), int(input())
ans = m * n
if m > 2 and n > 2:
    ans -= (m - 2) * (n - 2)
print(ans)