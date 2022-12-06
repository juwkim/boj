def is_prime(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i**2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
    return True

a, b = input().split()
first, second = map(int, [a, b + a])
print('Yes' if is_prime(first) and is_prime(second) else 'No')