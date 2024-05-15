from itertools import pairwise

n, x, y = map(int, input().split())
t = []
for _ in range(n):
    h, m = map(int, input().split(':'))
    t.append(h * 60 + m)
t.append(23 * 60 + 59)
ans = 100
for i, (a, b) in enumerate(pairwise(t)):
    diff = b - a
    if i&1:
        ans = min(100, ans + 100 * diff / y)
    else:
        ans = max(0, ans - 100 * diff / x)
print(ans)