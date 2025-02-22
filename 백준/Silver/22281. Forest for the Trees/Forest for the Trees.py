from math import gcd

xb, yb, x1, y1, x2, y2 = map(int, open(0).read().split())
g = gcd(xb, yb)
xd, yd = xb // g, yb // g
xl, xr = (x1 + xd - 1) // xd, x2 // xd
yl, yr = (y1 + yd - 1) // yd, y2 // yd
l, r = max(xl, yl), min(xr, yr)
if g == 1 or l == 1 and xd * (r + 1) >= xb:
    print("Yes")
else:
    print("No")
    if l == 1:
        print(xd * (r + 1), yd * (r + 1))
    else:
        print(xd, yd)