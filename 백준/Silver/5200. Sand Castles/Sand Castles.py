from math import pi
for tc in range(1, 1 + int(input())):
    *l, b = input().split()
    w, h, m, d = map(float, l)
    sand = (w * h - (w - 2 * m) * (h - 2 * m)) * d
    for _ in range(int(b)):
        hi, ri = map(float, input().split())
        sand -= pi * ri * ri * hi
    
    ans = sand / (w * h)
    print(f'Data Set {tc}:\n{ans:.2f}')