import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    n, h = g()
    a = g()
    b = g()
    ans = 0
    l, r = 0, 0
    cnt, tunnel = 0, 0
    while r < n:
        tunnel += a[r]
        cnt += b[r]
        while tunnel - a[l] >= h:
            tunnel -= a[l]
            cnt -= b[l]
            l += 1
        if cnt == 0:
            ans += 1
            cnt += 1
            b[r] = 1
        r += 1
    if b[-1] == 0:
        ans += 1
    print(ans)