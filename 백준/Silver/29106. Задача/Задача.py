import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

n, k = g()
a = sorted(g())
l, r = 0, k - 1
p, q = l, r
while r < n:
    if a[r] - a[l] < a[q] - a[p]:
        p, q = l, r
    l += 1
    r += 1
print(*a[p:q + 1])