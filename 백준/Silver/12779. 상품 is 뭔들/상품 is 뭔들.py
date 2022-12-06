from math import gcd
a, b = map(int, input().split())
a += 1
s = int(b**.5) - int((a)**.5) + (int(a**.5)**2 == a)

if s:
    t = gcd(s, b - a + 1)
    print(f'{s//t}/{(b-a+1)//t}')
else:
    print(0)