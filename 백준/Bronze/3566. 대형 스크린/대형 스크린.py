from math import ceil
c_rh, c_rv, c_sh, c_sv = map(int, input().split())
min_price = 10**10
for _ in range(int(input())):
    rh, rv, sh, sv, p = map(int, input().split())
    a = ceil(max(c_rh/rh, c_sh/sh)) * ceil(max(c_rv/rv, c_sv/sv))
    b = ceil(max(c_rh/rv, c_sh/sv)) * ceil(max(c_rv/rh, c_sv/sh))
    min_price = min(min_price, min(a, b) * p)
print(min_price)