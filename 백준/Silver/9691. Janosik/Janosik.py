n = int(input())
a, i = 0, 2
while i <= n:
    e = min(n - i, i - 1)
    a += e * (e + 1)
    i *= 2
print(a >> 1)