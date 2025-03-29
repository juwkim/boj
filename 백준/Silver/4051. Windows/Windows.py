import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

tc = 1
while n:=int(input()):
    windows = [g() for _ in range(n)]
    print(f"Desktop {tc}:")
    for _ in range(int(input())):
        cr, cc = g()
        ans = "background"
        for k in range(n - 1, -1, -1):
            r, c, h, w = windows[k]
            if r <= cr < r + w and c <= cc < c + h:
                ans = f"window {k + 1}"
                break
        print(ans)
    tc += 1