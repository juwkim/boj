from math import dist
for l in open(0):
    x1, y1, x2, y2, x3, y3 = map(float, l.split())
    a, b, c = dist((x2, y2), (x3, y3)), dist((x1, y1), (x3, y3)), dist((x1, y1), (x2, y2))
    print("%.2f" % (3.141592653589793 * a * b * c / abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))))