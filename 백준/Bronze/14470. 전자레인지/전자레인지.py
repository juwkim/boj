import sys
A, B, C, D, E = map(int, sys.stdin.read().split())
print(E * (B - A) if A > 0 else - A * C + D + E * B)