n, k = map(int, input().split())
if k > n * n - n or (n, k) == (2, 2):
    print("NO")
else:
    print("YES")
    a = [['.'] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if k == 0:
                break
            if i + j != n - 1:
                a[i][j] = '#'
                k -= 1
        if k == 0:
            break
    if a[0][0] == '#':
        a[0][0], a[n - 1][0] = '.#'
    if a[n - 1][n - 1] == '#':
        a[0][n - 1], a[n - 1][n - 1] = '#.'
    for l in a:
        print(*l, sep='')