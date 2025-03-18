n, p, q = map(int, input().split())
print((q * (p + n - q + 1) - p * p) % 123456789)