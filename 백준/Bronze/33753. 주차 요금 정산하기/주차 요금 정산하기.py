A, B, C, T = map(int, open(0).read().split())
print(A + max(0, (T + B - 31) // B) * C)