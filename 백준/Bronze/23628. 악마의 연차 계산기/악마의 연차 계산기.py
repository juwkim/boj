g = lambda: [*map(int, input().split())]

y1, m1, d1 = g()
y2, m2, d2 = g()

day = (y2 - y1) * 360 + (m2 - m1) * 30 + d2 - d1
year = day // 360
p = year // 2
year_off = p * (29 + p) + (15 + p) * (year % 2)
month_off = min(36, day // 30)

print(year_off, month_off)
print("%ddays" % (day))