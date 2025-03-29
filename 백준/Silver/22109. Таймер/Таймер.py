import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y, k, t = map(int, input().split())
    r = (x - 1) % y + 1
    if t - y + r >= k:
        x += y * k + (t - k)
    else:
        x += (y - 1) * min(k - 1, t) + t + y - r
    print(x)