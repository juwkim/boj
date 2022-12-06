a, b, n, w = map(int, input().split())
if a != b:
    k = (w - b*n) / (a - b)
    if k == int(k) and 1 <= k <= n - 1:
        print(int(k), n - int(k))
    else:
        print(-1)
elif a == b and w == b*n and n == 2:
    print(1, 1)
else:
    print(-1)