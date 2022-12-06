from math import gcd
N, M = map(int, input().split())
print(M - gcd(N, M))