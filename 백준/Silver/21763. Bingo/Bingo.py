n, k = map(int, input().split())
if k > n * n - n:
    print("NO")
else:
    print("YES")
    a = [['.'] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if k == 0:
                break
            if i != j:
                a[i][j] = '#'
                k -= 1
        if k == 0:
            break
    for l in a:
        print(*l, sep='')