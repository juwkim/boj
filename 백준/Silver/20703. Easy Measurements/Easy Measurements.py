import sys
input = sys.stdin.readline
from math import lcm

for _ in range(int(input())):
    b, d = map(int, input().split())
    l = lcm(b, d)
    c = (b - l) % (l // b)
    if c == 0:
        c += l // b
    print(len(range(c, b, l // b)))