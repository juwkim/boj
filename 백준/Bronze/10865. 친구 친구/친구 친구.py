import sys
N, M = map(int, input().split())
a = [0] * (N+1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    a[A] += 1
    a[B] += 1
print(*a[1:])