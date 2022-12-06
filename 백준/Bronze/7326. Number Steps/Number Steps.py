import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == y:
        print(2 * x - x % 2)
    elif x == y + 2:
        print(2 * x - 2 - x % 2)
    else:
        print('No Number')