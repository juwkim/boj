import sys
input = sys.stdin.readline
from fractions import Fraction
for _ in range(int(input())):
    K, M, x = input().split()
    print(K, Fraction(x).limit_denominator(int(M)))