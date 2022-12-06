n, k, i, j = map(int, input().split())
if i > k:
    print((i + j - 2 * k) * (j - i + 1) // 2)
elif j <= k:
    print((i + j + 2 * n - 2 * k) * (j - i + 1) // 2)
else:
    p = (2 * n + i - k) * (k - i + 1) // 2
    q = (j - k + 1) * (j - k) // 2
    print(p + q)