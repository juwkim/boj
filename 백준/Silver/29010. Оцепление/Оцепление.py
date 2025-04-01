n, m, k = map(int, input().split())
if k > n + m - 3:
    print("NO")
else:
    a = [['.' for _ in range(m)] for _ in range(n)]
    q, r = divmod(k, 2)
    for i in range(n):
        for j in range(m):
            if 0 < i + j <= q + r or 0 < n + m - i - j - 2 <= q:
                a[i][j] = 'C'
    print("YES")
    for l in a:
        print(*l, sep='')