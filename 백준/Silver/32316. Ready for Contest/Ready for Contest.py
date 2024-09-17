import sys
g = lambda: map(int, sys.stdin.readline().split())

n, m = g()
a = [set() for _ in range(n + 1)]
for _ in range(m):
    p, L = g()
    if L != 3:
        a[p].add(L)
for i in range(1, n + 1):
    if a[i] == {1, 2}:
        print(i)