import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

a, b = int(input()), int(input())
d = abs(a - b)
if d&1:
    print("Error")
elif min(a, b) >= 2:
    print("Undefined")
else:
    print(max(0, (a - b) // 2))
    print(max(0, (b - a) // 2))
    print(min(a, b))