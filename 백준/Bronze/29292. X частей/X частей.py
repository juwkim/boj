g = lambda: [*map(int, input().split())]

n, X = g()
a, b = g(), g()
i = 0
for num in b:
    cur = 0
    while i < n and cur < num:
        cur += a[i]
        i += 1
    if cur < num:
        print(-1)
        break
else:
    print(sum(a) - sum(b))