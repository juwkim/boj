from math import isqrt
for step in range(1, 1 + int(input())):
    ans = 0
    A = int(input())
    for divisor in range(1, 1 + isqrt(A)):
        q, r = divmod(A, divisor)
        if r:
            continue
        ans += str(divisor) == str(divisor)[::-1]
        if divisor != q:
            ans += str(q) == str(q)[::-1]
    print(f'Case #{step}: {ans}')