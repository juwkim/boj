import sys
for line in sys.stdin:
    a, b, c = map(int, line.split())
    if (a, b, c) == (0, 0, 0):
        break
    if b - a == c - b:
        print('AP', 2 * c - b)
    else:
        print('GP', c**2 // b)