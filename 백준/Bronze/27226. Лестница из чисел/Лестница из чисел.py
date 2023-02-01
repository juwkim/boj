a, b, k = map(int, open(0))
for i in range(a, b + 1):
    s = i * (i - 1) // 2 + 1
    print(*range(s, s + min(i, k)))