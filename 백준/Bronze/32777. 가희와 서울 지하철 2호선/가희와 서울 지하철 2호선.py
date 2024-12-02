import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    if (b - a) % 43 < (a - b) % 43:
        print("Inner circle line")
    else:
        print("Outer circle line")