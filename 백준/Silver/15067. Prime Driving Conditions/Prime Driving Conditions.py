from bisect import bisect_left

def seive(n):
    prime = [True]*(n+1)
    prime[0] = prime[1] = False
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    return [i for i in range(2, n + 1) if prime[i]]

prime = seive(9973)
for l in [*open(0)][:-1]:
    a, b = l.split()
    if b > "9973":
        num = (ord(a[0]) - 65) * 26**2 + (ord(a[1]) - 65) * 26 + ord(a[2]) - 64
        s = chr(num // 26**2 + 65) + chr(num // 26 % 26 + 65) + chr(num % 26 + 65)
        print(s, "0002")
    else:
        print(f"{a} {prime[bisect_left(prime, int(b))]:04d}")