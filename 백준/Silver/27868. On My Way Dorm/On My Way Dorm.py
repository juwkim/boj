import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, S = g()
A = g()
print(input()[::-1])