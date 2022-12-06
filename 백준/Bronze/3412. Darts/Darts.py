g = lambda: [*map(int, input().split())]

import math
for _ in range(int(input())):
    score = 0
    n = int(input())
    for _ in range(n):
        x, y = g()
        p = math.ceil((x*x + y*y)**.5 / 20)
        score += max(0, min(10, 11 - p))
    print(score)