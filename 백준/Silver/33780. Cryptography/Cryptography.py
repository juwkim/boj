def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(n**.5) + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(input())
if is_prime(n):
    print("SAFE")
else:
    print("BROKEN")