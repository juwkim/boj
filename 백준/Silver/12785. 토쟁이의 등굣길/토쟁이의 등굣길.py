from math import comb

w, h, x, y = map(int, open(0).read().split())
print(comb(x + y - 2, x - 1) * comb(w + h - x - y, w - x) % 1000007)