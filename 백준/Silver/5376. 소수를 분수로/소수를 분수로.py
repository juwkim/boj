from math import gcd
for _ in range(int(input())):
    s = input().split('(')
    if len(s) == 1:
        b = s[0][2:]
        l1 = len(b)
        s = pow(10, l1)
        
        GCD = gcd(int(b), s)
        print("%d/%d" % (int(b) // GCD, s // GCD))
    else:
        b, c = s[0][2:], s[1][:-1]
        l1, l2 = len(b), len(c)
        s, t = pow(10, l1), pow(10, l2)
        
        p = (pow(10, l2) - 1) * (int(b) if b else 0) + int(c)
        q = pow(10, l1) * (pow(10, l2) - 1)
        
        GCD = gcd(p, q)
        print("%d/%d" % (p // GCD, q // GCD))