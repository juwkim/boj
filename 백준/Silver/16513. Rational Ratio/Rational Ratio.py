from math import gcd
s, t = input().split()
a, b = s.split('.')
l = len(b) - (t:=int(t))
n = int(b[l:]) + (10**t - 1) * (int(b[:l] if l else 0))
m = (10**t - 1) * 10**l
g = gcd(n, m)
n //= g
m //= g
print(f"{m*int(a)+n}/{m}")