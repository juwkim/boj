import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    A, B, X = g()
    W = A * (X - 1) + B
    print(W)