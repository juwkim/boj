import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

w, h = g()
n, a, b = g()
if a > w or b > h:
    print(-1)
else:
    one = (w // a) * (h // b)
    ans = (n + one - 1) // one
    print(ans)