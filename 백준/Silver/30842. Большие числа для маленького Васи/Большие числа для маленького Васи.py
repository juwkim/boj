import math

N, M = map(int, input().split())
print(input() * min(math.gcd(N, M), 10**6))