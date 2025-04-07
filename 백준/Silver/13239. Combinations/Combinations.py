import sys
input = sys.stdin.readline
from math import comb

for _ in range(int(input())):
    print(comb(*map(int, input().split())) % 1000000007)