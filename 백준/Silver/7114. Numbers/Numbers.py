import math
g = lambda: [*map(int, input().split())]
a, b, c, d = g()
if a and b:
    pass
elif a and c:
    b = c // (a * a)
elif a and d:
    b = - math.isqrt(d // a)
elif b and d:
    a = d // (b * b)
elif b and c:
    a = - math.isqrt(c // b)
    if a < b:
        a *= -1
elif c and d:
    a_cubic = c * c // d
    a_cubic_abs = abs(a_cubic)
    a = 1
    while a ** 3 != a_cubic_abs:
        a += 1
    if a_cubic < 0:
        a *= -1
    b = c // (a * a)
elif a:
    b = -999
elif b:
    a = b
elif c:
    flag = False
    for a in range(-999, 1000):
        tmp = a * a
        for b in range(-999, a+1):
            if tmp * b == c:
                flag = True
                break
        if flag:
            break
elif d:
    flag = False
    for a in range(-999, 1000):
        for b in range(-999, a+1):
            if a * b * b == d:
                flag = True
                break    
        if flag:
            break
else:
    a = -999
    b = -999

c = a * a * b
d = a * b * b
print(a, b, c, d)