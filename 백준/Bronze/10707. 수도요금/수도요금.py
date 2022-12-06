import sys
A, B, C, D, P = map(int, sys.stdin.read().split())
print(min(A * P, B + D * max(P - C, 0)))