import sys
from math import log
while s:= sys.stdin.readline():
    N, B, M = map(float, s.split())
    print(1 + int(log(M/N, 1+B/100)))