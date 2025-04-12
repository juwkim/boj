X = int(input())
p = (2 * X + .25)**.5 - .5
i = int(p) + (not p.is_integer())
num = X - i * (i - 1) // 2
if i & 1:
    a, b = i + 1 - num, num
else:
    a, b = num, i + 1 - num
print(f"{a}/{b}")