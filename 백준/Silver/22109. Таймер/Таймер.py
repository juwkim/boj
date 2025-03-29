import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y, k, t = map(int, input().split())
    r = x % y
    if r == 0:
        r = 1
        x += 1
        t -= 1
    if t - y + r >= k:
        x += y * k + (t - k)
    else:
        x += y - r
        k -= 1
        cnt = min(k, t)
        x += y * cnt + (t - cnt)
    print(x)