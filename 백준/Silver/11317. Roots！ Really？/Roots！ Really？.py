import sys
input = lambda: sys.stdin.readline().rstrip()


g = lambda: [*map(int, input().split())]
from math import sqrt
for _ in range(int(input())):
    a, b, c, s, t = g()
    
    D = b * b - 4 * a * c
    if D < 0:
        print('No')
    else:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        
        if s <= x1 <= t or s <= x2 <= t:
            print('Yes')
        else:
            print('No')