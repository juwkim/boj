import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N = int(input())
A = g()
for _ in range(N - 1):
    A = min(A, g())
B = g()
for _ in range(N - 1):
    B = min(B, g())
print(B[0] - A[0], B[1] - A[1])