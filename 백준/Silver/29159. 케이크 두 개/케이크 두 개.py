import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import gcd

A = [g() for _ in range(4)]
B = [g() for _ in range(4)]
a = sum(B[i][1] for i in range(4)) - sum(A[i][1] for i in range(4))
b = sum(B[i][0] for i in range(4)) - sum(A[i][0] for i in range(4))
if b < 0:
    a, b = -a, -b
GCD = gcd(a, b)
a //= GCD
b //= GCD
if b == 1:
    print(f"{a}", end=" ")
else:
    print(f"{a}/{b}", end=" ")
    
x = sum(A[i][0] for i in range(4))
y = sum(A[i][1] for i in range(4))
p = b * y - a * x
q = 4 * b
GCD = gcd(p, q)
p //= GCD
q //= GCD
if q == 1:
    print(f"{p}")
else:
    print(f"{p}/{q}")