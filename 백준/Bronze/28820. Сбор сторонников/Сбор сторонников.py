from math import lcm

l, s, *d = map(int, open(0).read().split())
print((s - 1 + lcm(*d)) % 7 + 1)