import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N = int(input())
a1, *a, a2 = g()
b1, *b, b2 = g()
if N == 2:
    if b1 > 0 and a2 > 0:
        print(a1 + b1 + a2 + b2)
    else:
        print(a1 + b2 + max(a2, b1))
else:
    s, t = a1 + a[0] + max(b1, 0), a1 + b1 + b[0]
    if N == 3:
        if a2 > 0 and b[-1] > 0:
            s = s + b2 + a2 + b[-1]
        else:
            s = s + b2 + max(a2, b[-1])
        t = t + b2 + max(a[-1], 0) + max(a2, 0)
    else:
        for i in range(1, N - 2):
            s, t = max(s + a[i] + max(b[i - 1], 0), t + a[i - 1] + a[i]), max(s + b[i - 1] + b[i], t + b[i] + max(a[i - 1], 0))
        if a2 > 0 and b[-1] > 0:
            s = s + b2 + a2 + b[-1]
        else:
            s = s + b2 + max(a2, b[-1])
        t = t + b2 + max(a[-1], 0) + max(a2, 0)
    print(max(s, t))