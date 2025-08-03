n, m = map(int, open(0))
print((n * 10**18 // (m + 1) + 1) // 10**18)
print(n // m)