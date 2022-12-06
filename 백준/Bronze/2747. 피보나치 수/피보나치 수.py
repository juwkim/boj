def fibonacci(n):
    if n < 2:
        return n
    else:
        return round((((1 + 5**0.5) / 2)**n - ((1 - 5**0.5) / 2)**n) / 5**0.5)

print(fibonacci(int(input())))