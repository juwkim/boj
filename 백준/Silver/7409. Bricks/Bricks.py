import math

def can_fit(w, h, x, y):
    if x <= w and y <= h or y <= w and x <= h:
        return True
    def fits(theta):
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        width = x * cos_t + y * sin_t
        height = x * sin_t + y * cos_t
        return width <= w and height <= h
    for i in range(10000):
        theta = i * math.pi / 20000
        if fits(theta):
            return True
    return False

A, B, C, D, E = map(float, input().split())
if any(can_fit(D, E, x, y) for x, y in ((A, B), (A, C), (B, C))):
    print("YES")
else:
    print("NO")