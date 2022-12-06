import sys
A, B, C, D = map(int, sys.stdin.read().split())
print(min(A + D, B + C))