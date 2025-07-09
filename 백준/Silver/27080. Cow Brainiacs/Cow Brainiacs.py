from collections import Counter

def factorize(b):
    factors = Counter()
    for i in range(2, 30):
        while b % i == 0:
            b //= i
            factors[i] += 1
    return factors

def cnt_p_in_factorial(n, p):
    cnt = 0
    while n:
        n //= p
        cnt += n
    return cnt

N, B = map(int, input().split())
factors = factorize(B)
pexp = {}
for p in factors:
    pexp[p] = cnt_p_in_factorial(N, p)

rem = 1
for i in range(1, N + 1):
    x = i
    for p in factors:
        while x % p == 0:
            x //= p
    rem = rem * x % B

min_power = min(pexp[p] // factors[p] for p in factors)
for p in factors:
    exp = pexp[p] - factors[p] * min_power
    rem = (rem * pow(p, exp, B)) % B
print(rem)