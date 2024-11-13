import sys
input = sys.stdin.readline
from math import isqrt

for _ in range(int(input())):
    N = int(input())
    print(("EMPTY", "O", "S", "OS")[(N & 1) + 2 * (isqrt(N) ** 2 == N)])