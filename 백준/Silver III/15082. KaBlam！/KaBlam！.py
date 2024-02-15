from math import sin, tan, atan, degrees, pi

xm, vx, vy, xa, va, tk = map(int, input().split())
p = vy * tk - 16 * tk ** 2
ans = "start running"
if p > 0:
    if xm - xa + vx * tk == 0:
        a = pi / 2
    else:
        a = atan(p / (xm - xa + vx * tk))
        if a < 0:
            a += pi
    tl = tk - p / (va * sin(a))
    if 0 < tl < tk:
        ans = f"{tl}, {degrees(a)}"
print(ans)