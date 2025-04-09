import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
import math

N, M = g()
a = 0
for w, v in sorted([g() for _ in range(N)], key=lambda x: -x[1] / x[0]):
    if M > w:
        a += v
        M -= w
    else:
        a = M * v + w * a
        b = w
        break
gcd = math.gcd(a, b)
print(f"{a // gcd}/{b // gcd}")