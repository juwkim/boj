g = lambda: map(int, input().split())
from bisect import bisect_left, bisect_right
n, m = g()
A = sorted(g())
for _ in range(m):
    cmd, *l = g()
    if cmd == 1:
        print(n - bisect_left(A, l[0]))
    elif cmd == 2:
        print(n - bisect_right(A, l[0]))
    else:
        print(bisect_right(A, l[1]) - bisect_left(A, l[0]))