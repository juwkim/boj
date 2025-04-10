from math import gcd

c1, _, c3, _, c5, c6 = map(int, input().split())
x2, x6 = gcd(c1, c5), gcd(c3, c6)
print(c1 // x2, x2, c5 // x2, c6 // x6, x6, c3 // x6)