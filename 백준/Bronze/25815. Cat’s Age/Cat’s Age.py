g = lambda: [*map(int, input().split())]

y, m = g()
age = 0
if y == 0:
    age = m * 15
elif y == 1:
    age = 180 + m * 9
else:
    age = 288 + (y - 2) * 48 + m * 4
r, q = divmod(age, 12)
print(r, q)