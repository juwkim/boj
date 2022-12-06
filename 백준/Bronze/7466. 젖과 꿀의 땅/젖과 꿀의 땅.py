g = lambda: [*map(int, input().split())]

from math import isqrt
A, B = g()
if A == 1 and B == 1:
    print(0)
elif A == 1:
    input()
    print(sum(g()))
elif B == 1:
    print(sum(g()))
else:
    num = sum(g()) ** 2 + sum(g()) ** 2
    print(isqrt(num-1)+1)