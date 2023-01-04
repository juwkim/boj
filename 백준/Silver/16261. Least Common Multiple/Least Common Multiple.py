input = __import__('sys').stdin.readline
from math import gcd, lcm
for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    LCM = lcm(a * d, b * c)
    GCD = gcd(LCM, b * d)
    print(LCM // GCD, b * d // GCD)