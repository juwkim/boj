x, y = map(int, input().split())
a = 100 - x
b = 100 - y

c = 100 - (a + b)
d = a * b
q, r = divmod(d, 100)

print(a, b, c, d, q, r)
print(c + q, r)