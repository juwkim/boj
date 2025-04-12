X = int(input())
p = (2 * X + .25)**.5 + .5
i = int(p) - p.is_integer()
n = X - i * (i - 1) // 2
a, b = n, i + 1 - n
if i & 1: a, b = b, a
print(f"{a}/{b}")