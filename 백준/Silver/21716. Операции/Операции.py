import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import gcd

def solve():
    s = input()
    if '.' not in s:
        return int(s), 1
    num1, b = s.split('.')
    num1 = int(num1)
    if b[0] == '(':
        num3 = int(b[1:-1])
        q = pow(10, len(b) - 2)
        return (q - 1) * num1 + num3, q - 1
    elif b[-1] != ')':
        num2 = int(b)
        p = pow(10, len(b))
        return p * num1 + num2, p
    else:
        idx = b.index('(')
        num2 = int(b[:idx])
        num3 = int(b[idx + 1:-1])
        p = pow(10, idx)
        q = pow(10, len(b) - idx - 2)
        return p * (q - 1) * num1 + (q - 1) * num2 + num3, p * (q - 1)

a1, b1 = solve()
a2, b2 = solve()
a = a1 * b2 + a2 * b1
b = b1 * b2
gcd = gcd(a, b)
a //= gcd
b //= gcd
print(f"{a}/{b}")