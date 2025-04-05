import sys
from math import lcm, gcd
input = sys.stdin.readline

N = int(input())
A, B = zip(*[map(int, input().split()) for _ in range(N)])
denom = lcm(*B)
numer = gcd(*[a * denom // b for a, b in zip(A, B)])
g = gcd(numer, denom)
print(numer // g, denom // g)