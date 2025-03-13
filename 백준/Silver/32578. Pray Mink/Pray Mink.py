def is_prime(num):
    return num > 1 and all(num % i for i in range(2, int(num ** 0.5) + 1))

def solve(x):
    if x < 10:
        return int(is_prime(x))
    s = str(x)
    if is_prime(x):
        return 1 + max(solve(int(s[:i] + s[i + 1:])) for i in range(len(s)))
    return 0

print(solve(int(input())))