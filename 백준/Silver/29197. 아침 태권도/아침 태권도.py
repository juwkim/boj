import sys
input = sys.stdin.readline
from math import gcd

s = set()
for _ in range(int(input())):
    a, b = map(int, input().split())
    g = gcd(a, b)
    s.add((a // g, b // g))
print(len(s))