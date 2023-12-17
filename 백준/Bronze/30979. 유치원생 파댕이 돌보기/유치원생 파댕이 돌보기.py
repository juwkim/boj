import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

T, N = int(input()), int(input())
F = sum(g())
if F >= T:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")