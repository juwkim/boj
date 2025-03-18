n, p, q = map(int, input().split())
print((p * (q - p) + q * (n - q + 1)) % 123456789)