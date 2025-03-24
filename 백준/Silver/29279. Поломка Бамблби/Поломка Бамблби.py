import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n = int(input())
a = g()
px = [0] * (n + 1)
for i in range(n):
    px[i + 1] = px[i] + (a[i] == 1)
for _ in range(int(input())):
    l, r = g()
    print(1 + (px[r] - px[l - 1] == r - l + 1))