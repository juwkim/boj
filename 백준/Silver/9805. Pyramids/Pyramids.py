from math import sqrt, sin, acos

a, b, c, d, e, f = map(int, input().split())
i1 = acos((a * a + b * b - d * d) / (2 * a * b))
i2 = acos((b * b + c * c - f * f) / (2 * b * c))
i3 = acos((c * c + a * a - e * e) / (2 * c * a))
i4 = (i1 + i2 + i3) / 2
ans = a * b * c * sqrt(sin(i4) * sin(i4 - i1) * sin(i4 - i2) * sin(i4 - i3)) / 3
print(ans)