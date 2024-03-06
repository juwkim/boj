import sys
g = lambda: map(int, sys.stdin.readline().split())

n, s = g()
for _ in range(n):
    l, r = g()
    s += l <= s <= r
print(s)