from collections import Counter

for _ in range(int(input())):
    N = int(input())
    exponents = Counter()
    i = 2
    while i * i <= N:
        while N % i == 0:
            exponents[i] += 1
            N //= i
        i += 1
    if N > 1:
        exponents[N] += 1
    print(max(exponents.values(), default=1))