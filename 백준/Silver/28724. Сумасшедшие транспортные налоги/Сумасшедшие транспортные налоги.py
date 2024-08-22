import sys
input = sys.stdin.readline
from bisect import bisect

n = int(input())
b, t = zip(*[[*map(int, input().split())] for _ in range(n)])
for _ in range(int(input())):
    q = int(input())
    print(q * t[bisect(b, q - 1) - 1])