import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N = int(input())
x1, y1 = g()
for _ in range(N - 2):
    input()
x2, y2 = g()
print(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)