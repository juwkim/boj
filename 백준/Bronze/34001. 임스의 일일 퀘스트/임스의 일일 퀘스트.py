L = int(input())
a = [0] * 6
g = [0] * 7
limit_a = [200, 210, 220, 225, 230, 235, 245, 250]
limit_g = 260
for i in range(6):
    if limit_a[i + 2] <= L:
        a[i] = 100
    elif limit_a[i + 1] <= L:
        a[i] = 300
    elif limit_a[i] <= L:
        a[i] = 500

for i in range(7):
    if limit_g + 10 <= L:
        g[i] = 100
    elif limit_g + 5 <= L:
        g[i] = 300
    elif limit_g <= L:
        g[i] = 500
    limit_g += 5

print(*a)
print(*g)