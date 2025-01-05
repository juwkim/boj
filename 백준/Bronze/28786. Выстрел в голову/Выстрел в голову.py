n, m, a, b = map(int, input().split())
ans = n
if a < b * m:
    q, r = divmod(n, m)
    ans += q * a
    if r: ans += min(a, r * b)
else:
    ans += n * b
print(ans)