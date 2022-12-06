def gcd(a, b):
    if a:
        return gcd(b%a, a)
    else:
        return b

while (s:=input()) != '0 0':
    a, b = sorted(map(int, s.split()))
    print(a * b // gcd(a, b)**2)