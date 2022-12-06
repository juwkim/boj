from math import floor
down = lambda x: max(x - 0.5, 0)
up = lambda x: x + 0.5
while (s:=input()) != '0 0 0 0':
    cal, fat, carb, prot = map(int, s.split())
    lo = floor(0.5 + 9 * down(fat) + 4 * (down(carb) + down(prot)))
    hi = floor(0.5 + 9 * up(fat) + 4 * (up(carb) + up(prot)))
    print('yes' if lo <= cal < hi else 'no')