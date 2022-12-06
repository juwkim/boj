g = lambda: [*map(int, input().split())]


from math import gcd
a, b = g()
c, d = g()

x = a * d + b * c
y = b * d

num = gcd(x, y)
print(x // num, y // num)