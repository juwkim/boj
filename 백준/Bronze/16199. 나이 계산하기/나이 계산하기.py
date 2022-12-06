import sys
y1, m1, d1, y2, m2, d2 = map(int, sys.stdin.read().split())
print(y2 - y1 - (d2 + 31 * m2 < d1 + 31 * m1))
print(y2 - y1 + 1)
print(y2 - y1)