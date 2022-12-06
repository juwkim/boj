n, m = map(int, input().split())
if n - 1 <= m <= 2 * n - 3:
    for i in range(2, n + 1):
        print(1, i)
    for i in range(2, 3 + m - n):
        print(i, n)
else:
    print(-1)