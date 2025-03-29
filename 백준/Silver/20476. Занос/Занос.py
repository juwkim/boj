v, x, y, a, b = map(int, input().split())
if v * v < 2 * b * x:
    t = v / (2 * b) + x / v
else:
    t = (2 * x / b) **.5
if v * v < 2 * a * y:
    t += v / (2 * a) + y / v
else:
    t += (2 * y / a) **.5
print(t)