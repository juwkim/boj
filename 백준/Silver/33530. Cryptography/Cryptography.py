n = int(input())
print(("BROKEN", "SAFE")[n > 1 and all(n % i for i in range(2, int(n**.5) + 1))])