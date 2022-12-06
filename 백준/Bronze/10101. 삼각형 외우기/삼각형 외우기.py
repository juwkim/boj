import sys
a, b, c = sorted(map(int, sys.stdin.read().split()))
s = a + b + c
if s != 180:
    print('Error')
else:
    if a == b == c == 60:
        print('Equilateral')
    elif a == b or b == c:
        print('Isosceles')
    else:
        print('Scalene')