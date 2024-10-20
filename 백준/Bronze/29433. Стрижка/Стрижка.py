n, k = map(int, input().split())
for i in range(n):
    print((i - 1) % k + 1, end=' ')