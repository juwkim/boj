n, m = map(int, input().split())
ans = 0
if m <= n:
    ans += n - 1
    n, m = m - 1, n
ans += n * (n - 1) // 2 + (m - 2 + m - n) * (n - 1) // 2
print(ans)