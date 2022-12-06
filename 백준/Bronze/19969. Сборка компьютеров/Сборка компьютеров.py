g = lambda: [*map(int, input().split())]

a = g()
b = g()
ans = 0
for i in range(2):
    Min = min(a[i], b[i])
    ans += Min
    a[i] -= Min
    b[i] -= Min
s = min(a[2], b[0] + b[1])
t = min(b[2], a[0] + a[1])
ans += min(a[2] + t, b[2] + s)
print(ans)