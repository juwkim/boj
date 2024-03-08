from math import gcd
s, t = input().split()
a, b = s.split('.')
t = int(t)
l = len(b) - t
n = int(b[l:])
if l:
    n += (10**t - 1) * (int(b[:l]))
m = (10**t - 1) * 10**l
g = gcd(n, m)
n //= g
m //= g
print(f"{m*int(a)+n}/{m}")