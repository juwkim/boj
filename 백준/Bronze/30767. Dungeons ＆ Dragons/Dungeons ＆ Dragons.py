n, a, b, c, d = map(int, open(0).read().split())

p = max(n - b, c)
q = min(n - a, d)
ans = max(0, q - p + 1)
print(ans)