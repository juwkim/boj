import sys
input = sys.stdin.readline
from math import lcm

for _ in range(int(input())):
    b, d = map(int, input().split())
    l = lcm(b, d)
    s = l // b
    c = (b - l - 1) % s + 1
    print((b - c + s - 1) // s)