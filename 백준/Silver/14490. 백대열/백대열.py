from math import gcd
n, m = map(int, input().split(':'))
a = gcd(n, m)
n //= a
m //= a
print(f'{n}:{m}')