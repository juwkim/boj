import sys
a, b, c, d = map(int, sys.stdin.read().split())
print(['answer', 'ignore'][a in [8, 9] and b == c and d in [8, 9]])