import sys
input = sys.stdin.readline
from math import hypot

for _ in range(int(input())):
    w, g, h, r = map(int, input().split())
    g, h = g - r, h - r
    print(hypot(w, h - g), hypot(w * g / (g + h), g) + hypot(w * h / (g + h), h) if g + h else w)