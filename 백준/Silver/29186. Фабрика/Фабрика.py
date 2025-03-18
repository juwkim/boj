import sys
input = sys.stdin.readline
from math import gcd

for _ in range(int(input())):
    a, b = sorted(map(int, input().split()))
    num = (a + b) // gcd(a, b)
    if num & (num - 1):
        print("NO")
    else:
        print("YES")