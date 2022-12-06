g = lambda: map(int, input().split())
a, b = g()
c, d = g()
if a <= c < b and b <= d:
    lap = b - c
elif a <= c and b >= d:
    lap = d - c
elif a >= c and a < d <= b:
    lap = d - a
elif a >= c and b <= d:
    lap = b - a
else:
    lap = 0
print(b + d - a - c - lap)