from math import gcd
s, t = input(), input()
a = gcd(len(s), len(t))
if s * (len(t) // a) == t * (len(s) // a):
    print(1)
else:
    print(0)