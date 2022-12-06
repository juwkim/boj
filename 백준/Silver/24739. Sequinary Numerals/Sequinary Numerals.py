from fractions import Fraction
ans = 0
r = Fraction(3, 2)
num = 1
for c in input()[::-1]:
    ans += num * int(c)
    num *= r
a, b = ans.as_integer_ratio()
if b == 1:
    print(a)
else:
    r, q = divmod(a, b)
    print(f'{r} {q}/{b}')