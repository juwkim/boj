order = 1
while(True):
    p, e, i, d = map(int, input().split())
    if (p, e, i, d) == (-1, -1, -1, -1):
        break
    b = 0
    while True:
        a = (28*b + e - p)/23
        if a == int(a):
            break
        b += 1
    b = 0
    while True:
        c = (23*a + p + 23*28*b - i)/33
        if c == int(c):
            break
        b += 1
    day = int(33*c + i - d)
    if day <= 0:
        day += 21252
    print(f'Case {order}: the next triple peak occurs in {day} days.')
    order += 1