from math import isqrt
while True:
    a, b = map(int, input().split())
    if a == 0:
        break
    ans = float('inf')
    for p in range(1, 1 + isqrt(a)):
        q, r1 = divmod(a, p)
        if r1:
            continue
        for s in range(1, 1 + isqrt(b)):
            t, r2 = divmod(b, s)
            if r2:
                continue
            n1, n2, n3, n4 = sorted([p, q, s, t])
            ans = min(ans, (n2 - n1)**2 + (n3 - n2)**2 + (n4 - n3)**2)
    print(ans)