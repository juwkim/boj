import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

h, l, a, b = g()
if (h * 2 >= a and l >= b) or (h * 2 >= b and l >= a):
    print('YES')
else:
    print('NO')