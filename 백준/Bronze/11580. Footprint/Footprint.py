input()
x, y = 0, 0
buf = {(0, 0)}
for c in input():
    x += (c == 'E') - (c == 'W')
    y += (c == 'S') - (c == 'N')
    buf.add((x, y))
print(len(buf))