from math import isqrt
for _ in range(int(input())):
    L, R = map(int, input().split())
    ans = 0
    for num in range(L, R + 1):
        cnt = 0
        for divisor in range(1, isqrt(num) + 1):
            r, q = divmod(num, divisor)
            if q == 0:
                cnt += 1 + (r != divisor)
        ans = max(ans, cnt)
    print(ans)