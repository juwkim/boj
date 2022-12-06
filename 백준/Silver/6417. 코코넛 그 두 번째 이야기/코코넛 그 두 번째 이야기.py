from math import isqrt
while (n:= int(input())) + 1:
    k = isqrt(n) + 1
    while k > 1:
        flag = True
        coconut = n
        for _ in range(k):
            r, q = divmod(coconut - 1, k)
            if q:
                flag = False
                break
            coconut -= r + 1
        if flag and coconut % k == 0:
            break
        k -= 1
    if flag:
        print(f'{n} coconuts, {k} people and 1 monkey')
    else:
        print(f'{n} coconuts, no solution')