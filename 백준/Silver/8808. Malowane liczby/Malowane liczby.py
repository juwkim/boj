import sys
input = lambda: sys.stdin.readline().rstrip()

from math import gcd
for _ in range(int(input())):
    a, b = sorted(map(int, input().split('/')))
    g = gcd(a, b)
    a, b = a // g, b // g
    change = 0
    while a != 1:
        change += b // a
        a, b = b % a, a
    print(['niebieski', 'czerwony'][(b + change)&1])