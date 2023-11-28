import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

A, B = g()
print(A * B // (A + B) if A and B else 0)