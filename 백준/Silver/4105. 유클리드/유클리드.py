def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
d = lambda p: (p[0] ** 2 + p[1] ** 2)**.5

for l in [*open(0)][:-1]:
    AX, AY, BX, BY, CX, CY, DX, DY, EX, EY, FX, FY = map(float, l.split())
    AB, AC = (BX - AX, BY - AY), (CX - AX, CY - AY)
    dAB, dAC = d(AB), d(AC)
    cos = (AB[0] * AC[0] + AB[1] * AC[1]) / (dAB * dAC)
    sin = (1 - cos ** 2) ** 0.5
    l = triangle_area(DX, DY, EX, EY, FX, FY) / (sin * dAB * dAC)
    dx, dy = AC[0] * l, AC[1] * l
    print("%.3f %.3f %.3f %.3f" % (BX + dx, BY + dy, AX + dx, AY + dy))