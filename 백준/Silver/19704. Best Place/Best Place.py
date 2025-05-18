import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n = int(input())
x, y = zip(*[g() for _ in range(n)])
print(sorted(x)[n >> 1], sorted(y)[n >> 1])