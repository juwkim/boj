n, r, k = map(int, input().split())
p = max(r, 2 * k - r)
print(p + r + max(0, n - p + (n - p & 1)))