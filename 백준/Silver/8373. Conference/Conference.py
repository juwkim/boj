import sys
g = lambda: map(int, sys.stdin.readline().split())

m, l, k, s = g()
c = [0] + [*g()]
book = [0] * (m + 1)
for _ in range(l):
    p, r = g()
    book[p] += r
ans = 0
for i in range(1, m + 1):
    q, r = divmod(book[i], k)
    ans += c[i] * (book[i] - r) - s * q + max(r * c[i] - s, 0)
print(ans)