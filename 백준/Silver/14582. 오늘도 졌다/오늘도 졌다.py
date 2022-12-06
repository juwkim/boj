g = lambda: [*map(int, input().split())]

a = g()
b = g()
s, t = 0, 0
ans = 'No'
for i in range(9):
    s += a[i]
    if s > t and s < t + b[i]:
        ans = 'Yes'
        break
    t += b[i]
print(ans)