import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, k = g()
m = int(input())
buf = sorted([g() for _ in range(m)], reverse=True)

ans = 0
filled = k
for l, r in buf:
    left = r - l + 1
    if filled != k:
        if left == filled:
            filled = k
            continue
        elif left < filled:
            filled -= left
            continue
        else:
            r -= filled
    div, mod = divmod(r - l + 1, k)
    ans += (2 * r - k * (div - 1)) * div
    if mod:
        filled = k - mod
        ans += 2 * (r - k * div)
    else:
        filled = k
print(ans)