import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
a1, b1 = g()
a2, b2 = g()
a3, b3 = g()
for x1 in range(a1 + 1):
    x2 = a1 + a2 - b3 - x1
    x3 = a3 - b2 + x1
    y1 = a1 - x1
    y2 = b3 - a1 + x1
    y3 = b2 - x1
    if x2 >= 0 and x3 >= 0 and y1 >= 0 and y2 >= 0 and y3 >= 0:
        print(1)
        print(x1, y1)
        print(x2, y2)
        print(x3, y3)
        break
else:
    print(0)