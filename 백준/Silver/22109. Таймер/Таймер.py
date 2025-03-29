import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y, k, t = map(int, input().split())
    r = (x - 1) % y + 1
    if t < k + y - r:
        x += (y - 1) * min(k - 1, t) + t + y - r
    else:
        x += (y - 1) * k + t
    print(x)