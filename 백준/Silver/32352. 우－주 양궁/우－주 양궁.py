g = lambda: map(int, input().split())

Xlo, Xhi, Ylo, Yhi, Zlo, Zhi = g()
xlo, xhi, ylo, yhi, zlo, zhi = g()
if xhi > Xlo and Xhi > xlo and yhi > Ylo and Yhi > ylo:
    print(max(0, Zlo - zhi + 1))
else:
    print(-1)