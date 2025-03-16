import sys
input = sys.stdin.readline
from math import isqrt

for _ in range(int(input())):
    S = (N:=input())[::-1]
    if int(N) == isqrt(int(N)) ** 2 and int(S) == isqrt(int(S)) ** 2:
        print("YES")
    else:
        print("NO")