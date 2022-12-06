g = lambda: [*map(int, input().split())]

from math import pi
while sum(s:= g()):
    D, V = s
    ans = (D ** 3 - 6 * V / pi) ** (1 / 3)
    print("%.3f" % ans)