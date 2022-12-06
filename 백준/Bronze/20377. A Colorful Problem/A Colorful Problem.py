g = lambda: [*map(int, input().split())]

import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]

color = [g() for _ in range(16)]

while True:
    try:
        r1, g1, b1 = map(int, input().split())
        r2, g2, b2 = min(color, key=lambda x: (x[0] - r1) ** 2 + (x[1] - g1) ** 2 + (x[2] - b1) ** 2)
        print(f'{r1:3d}{g1:4d}{b1:4d} maps to{r2:4d}{g2:4d}{b2:4d}')
    except:
        break