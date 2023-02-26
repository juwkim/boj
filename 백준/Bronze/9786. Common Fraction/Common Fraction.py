from fractions import Fraction
for _ in range(int(input())):
    a = Fraction(*map(int, input().split()))
    print(a.numerator, a.denominator)