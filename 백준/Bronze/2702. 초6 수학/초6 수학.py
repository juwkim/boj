from math import *
for _ in range(int(input())):
    A, B = map(int, input().split())
    s = gcd(A, B)
    print(int(A*B/s), s)