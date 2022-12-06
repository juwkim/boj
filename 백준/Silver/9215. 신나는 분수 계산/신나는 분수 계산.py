from math import gcd

cnt = 0
while (n := int(input())):
    
    cnt += 1
    a, b, c = [], [], []
    for _ in range(n):
        s = input()
        if ',' in s:
            w, p = s.split(',')
            n, d = map(int, p.split('/'))
            a.append(int(w))
            b.append(n)
            c.append(d)
        elif '/' in s:
            n, d = map(int, s.split('/'))
            b.append(n)
            c.append(d)
        else:
            a.append(int(s))
    
    if c:
        x = 1
        for num in c:
            x *= num // gcd(x, num)
        for i in range(len(b)):
            b[i] *= x // c[i]
        r, q = divmod(sum(b), x)
        r += sum(a)
        
        l = gcd(x, q)
        x //= l
        q //= l
        
        if r and q:
            print(f'Test {cnt}: {r},{q}/{x}')
        elif q:
            print(f'Test {cnt}: {q}/{x}')
        else:
            print(f'Test {cnt}: {r}')
    else:
        print(f'Test {cnt}:', sum(a))