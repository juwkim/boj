import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = 0, 0
for _ in range(int(input())):
    s = input()
    idx = s.find(',')
    if idx == -1:
        a += int(s)
    else:
        p, q = s.split(',')
        a += int(p)
        if p[0] == '-':
            b -= int(q) * pow(10, 100 - len(q))
        else:
            b += int(q) * pow(10, 100 - len(q))
if b > 0:
    q, r = divmod(b, pow(10, 100))
    a += q
    if a < 0 and r:
        if a < -1:
            a += 1
        else:
            a = "-0"
        r = pow(10, 100) - r
else:
    q, r = divmod(-b, pow(10, 100))
    a -= q
    if a >= 0 and r:
        if a > 0:
            a -= 1
            r = pow(10, 100) - r
        else:
            a = "-0"
if r:
    print(a, str(r).zfill(100).rstrip('0'), sep=',')
else:
    print(a)