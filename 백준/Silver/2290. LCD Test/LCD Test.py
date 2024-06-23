s, n = input().split()
s = int(s)
n = [*map(int, n)]
x, y = ' ' * (s + 2), ' ' + '-' * s + ' '
f, g, h, r = ' ' * (s + 2), ' ' * (s + 1) + '|', '|' + ' ' * (s + 1), '|' + ' ' * s + '|'
a = (y, x, y, y, x, y, y, y, y, y, y)
b = (r, g, g, g, r, h, h, g, r, r, h)
c = (x, x, y, y, y, y, y, x, y, y, y)
d = (r, g, h, g, g, g, r, g, r, g, h)
e = (y, x, y, y, x, y, y, x, y, y, y)
print(*[a[i] for i in n])
p = [b[i] for i in n]
for _ in range(s): print(*p)
print(*[c[i] for i in n])
q = [d[i] for i in n]
for _ in range(s): print(*q)
print(*[e[i] for i in n])