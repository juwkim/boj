import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, m = g()
for diff, gain in sorted((b - a, a) for a, b in zip(g(), g())):
    if diff > m:
        break
    m += gain
print(m)