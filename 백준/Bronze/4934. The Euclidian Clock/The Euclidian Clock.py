g = lambda: [*map(int, input().split())]

import math
for i in range(1, 1 + int(input())):
    h1, m1, s1, u1 = g()
    h2, m2, s2, u2 = g()
    r = float(input())
    
    t1 = ((h1 * 60 + m1) * 60 + s1) * 100 + u1
    t2 = ((h2 * 60 + m2) * 60 + s2) * 100 + u2
    
    half_day = 4_320_000
    time = (t2 - t1) % half_day
    
    ans = math.pi * r * r * time / half_day
    print(f'{i}. {ans:.3f}')