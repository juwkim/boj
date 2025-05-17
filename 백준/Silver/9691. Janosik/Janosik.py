n = int(input())
a, i = 0, 2
while i <= n:
    a += (2 * min(n - i, i - 1) + 1)**2 // 8
    i *= 2
print(a)