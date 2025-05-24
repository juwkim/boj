import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    dist = 0
    while a != b:
        if a > b:
            a >>= 1
        else:
            b >>= 1
        dist += 1
    print(dist)