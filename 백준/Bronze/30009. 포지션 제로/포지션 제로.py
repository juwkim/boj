import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

A, B = 0, 0
N = int(input())
X, Y, R = g()
for _ in range(N):
    T = int(input())
    A += X - R < T < X + R
    B += X - R == T or X + R == T
print(A, B)