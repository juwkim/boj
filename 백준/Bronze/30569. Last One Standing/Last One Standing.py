import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

h1, d1, t1 = g()
h2, d2, t2 = g()

one = (h2 - 1) // d1 * t1
two = (h1 - 1) // d2 * t2
if one < two:
    print("player one")
elif two < one:
    print("player two")
else:
    print("draw")