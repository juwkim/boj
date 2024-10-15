import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

n, d = g()
a = g()
b = g()
ans1 = n
for i in range(n):
    t = b[:i] + a[n - i:n] + [a[j] + b[i + j] for j in range(n - i)]
    if max(t) <= d:
        ans1 = i
        break
a, b = b, a
ans2 = n
for i in range(n):
    t = b[:i] + a[n - i:n] + [a[j] + b[i + j] for j in range(n - i)]
    if max(t) <= d:
        ans2 = i
        break
print(min(ans1, ans2))