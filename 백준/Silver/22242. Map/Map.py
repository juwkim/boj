dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
x, y = 0, 0
d, num = None, 0

for c in input():
    if c.isnumeric():
        num = num * 10 + int(c)
    else:
        if d != None:
            x += dx[d] * num
            y += dy[d] * num

        d, num = None, 0
        if c in 'wens':
            d = 'wens'.index(c)

if d != None:
    x += dx[d] * num
    y += dy[d] * num    

print("%.2f" % (x ** 2 + y ** 2) ** .5)