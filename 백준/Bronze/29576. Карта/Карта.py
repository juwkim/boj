n, k = map(int, input().split())
if k == 1:
    print((-1, 0)[n == 1])
elif (n - 1) % (k - 1) == 0:
    print((n - 1) // (k - 1))
else:
    print(-1)