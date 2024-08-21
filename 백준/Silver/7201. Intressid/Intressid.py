p, d, n = map(float, input().split())
cur, year = 0, 1
r = d * n / 100 / ((1 + n / 100) ** (1 / 12) - 1)
while (interest:=round(cur * n / 100 + r - d * 12, 2)) < 12 * (p - d):
    cur += d * 12 + interest
    year += 1
print(year)