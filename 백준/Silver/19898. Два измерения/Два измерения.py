l, r, a = map(int, open(0))
s, t = divmod(r - l + 1, a)
print(s * (2 * t + s * a - a) >> 1)