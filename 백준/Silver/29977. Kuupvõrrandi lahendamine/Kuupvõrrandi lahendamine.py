from math import isqrt

b, c, d = map(int, input().split())
def solve():
    if d == 0:
        return 0
    for i in range(1, int(abs(d)**.5) + 1):
        j, r = divmod(d, i)
        if r: continue
        for k in (i, j, -i, -j):
            if k**3 + b * k**2 + c * k + d == 0:
                return k

x1 = solve()
s = -x1 - b
t = d // x1 if x1 else c
num = s * s + 4 * t
if num == 1:
    if s & 1:
        x2, x3 = s >> 1, s + 1 >> 1
    else:
        x2, x3 = f"{s - 1}/2", f"{s + 1}/2"
elif num % 4 == 0 and num >= 0 and num == isqrt(num)**2:
    x2, x3 = s // 2 - isqrt(num), s // 2 + isqrt(num)
else:
    p = (s >> 1, f"{s}/2")[s & 1]
    if num % 4 == 0:
        q = f"{num >> 2}"
    elif num % 2 == 0:
        q = f"{num >> 1}/2"
    else:
        q = f"{num}/4"
    x2, x3 = f"{p}-sqrt({q})", f"{p}+sqrt({q})"
print(x1, x2, x3)