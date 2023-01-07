from math import dist
def g(): return [*map(int, input().split())]

d = 0
pos = g()
x, y = pos
while True:
    try:
        x1, y1, x2, y2 = g()
        d += dist((x1, y1), (x2, y2))
    except:
        break

h, m = divmod(round(d * 2 * 60 / (1000 * 20) + .5), 60)
print("%d:%02d" % (h, m))