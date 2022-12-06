g = lambda: [*map(int, input().split())]

from math import isqrt
for _ in range(int(input())):
    *l, S = g()
    a, b = sorted(l)
    ans = 'NO'
    for i in range(1, 1 + min(a, isqrt(S))):
        r, q = divmod(S, i)
        if q == 0 and r <= b:
            ans = 'YES'
            break
    print(ans)