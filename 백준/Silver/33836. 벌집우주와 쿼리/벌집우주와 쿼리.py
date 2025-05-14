import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x >= 0 and y == 0:
        print(0)
    elif x >= 0 or y == 0 or x >= y:
        print(1)
    else:
        print(2)