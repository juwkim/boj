import sys
input = sys.stdin.readline
from math import gcd

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    print(+(gcd(x1, y1) == gcd(x2, y2)))