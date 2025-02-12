n = int(input())

if n & 1:
    print((n - 1) // 6 * 2 + 1, n)
else:
    print((n - 2) // 6 * 2 + 2, n)