from fractions import Fraction

ans = 1
for i in range(2, int(input()) + 1):
    ans += Fraction(1, i)
print(ans.numerator, ans.denominator)