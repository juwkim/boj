n, m, p = map(int, input().split())
ans = 0
for w in range(n, 0, -1):
    h = max(1, (p + 1) // 2 - w)
    if h > m:
        break
    ans += (n + 1 - w) * (m + 1 - h) * (m + 2 - h) // 2
print(ans)