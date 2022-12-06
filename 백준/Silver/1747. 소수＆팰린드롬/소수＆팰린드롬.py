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

N = int(input())
while True:
    if str(N) == str(N)[::-1] and is_prime(N):
        print(N)
        break
    N += 1