from statistics import median
while (s:=input()) != '0 0 0 0':
    mw, mi, tw, ti = map(float, s.split())
    ew, ei = 4.19*mw*tw, 2.09*mi*ti - 335*mi
    e, m = ew + ei, mw + mi
    if e < -335*m:
        tem = (e+335*m)/m/2.09
    elif e < 0:
        tem = 0
    else:
        tem = e/m/4.19
    ice = abs(median([0, m, - e/335]))
    water = m - ice
    print(f'{ice:#.1f} g of ice and {water:#.1f} g of water at {tem:#.1f} C')