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
if x1:
    s, t = -x1 - b, d // x1
else:
    s, t = -b, c
num = s * s + 4 * t
if num == 1:
    if s & 1:
        x2 = s >> 1
        x3 = s + 1 >> 1
    else:
        x2 = f"{s - 1}/2"
        x3 = f"{s + 1}/2"
elif num % 4 == 0 and num >= 0 and num == isqrt(num)**2:
    x2 = s // 2 - isqrt(num)
    x3 = s // 2 + isqrt(num)
else:
    p = (s >> 1, f"{s}/2")[s & 1]
    if num % 4 == 0:
        q = f"sqrt({num >> 2})"
    elif num % 2 == 0:
        q = f"sqrt({num >> 1}/2)"
    else:
        q = f"sqrt({num}/4)"
    x2 = f"{p}-{q}"
    x3 = f"{p}+{q}"
print(x1, x2, x3)