import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import isqrt, log, sin

x = [1]
for i in range(1, 1000001):
    x.append((x[i - isqrt(i - 1) - 1] + x[int(log(i))] + x[int(i * sin(i) * sin(i))]) % 1000000)
while (i:=int(input())) != -1:
    print(x[i])