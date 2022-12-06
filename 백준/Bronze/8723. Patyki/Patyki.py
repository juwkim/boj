a, b, c = sorted(map(int, input().split()))
print(2 if a == b == c else 1 if a**2 + b**2 == c**2 else 0)