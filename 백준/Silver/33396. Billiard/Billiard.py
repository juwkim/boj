import sys
input = sys.stdin.readline
from math import lcm

for _ in range(int(input())):
    print(lcm(*map(int, input().split())) << 1)