def pq_extention(p, q, n):
    extention = ''
    while n:
        n, a = divmod(q*n, p)
        extention = expression(a) + extention
    return extention

def expression(a):
    if a < 10:
        return chr(a + 48)
    elif a < 36:
        return chr(a + 55)
    else:
        return chr(a + 61)

def back(a):
    if a <= '9':
        return ord(a) - 48
    elif a <= 'Z':
        return ord(a) - 55
    else:
        return ord(a) - 61


p, q, n = map(int, input().split())
a, b = divmod(n, q)
s, t = pq_extention(p, q, a), pq_extention(p, q, a+1)
if s and back(s[-1]) + b < p:
    print(s[:-1] + expression(back(s[-1]) + b))
else:
    print(t[:-1] + expression(back(t[-1]) - q + b))