from math import factorial

while (N := int(input())) != -1:
    print(f"N={N}:")
    print(factorial(N - 1) << 1)