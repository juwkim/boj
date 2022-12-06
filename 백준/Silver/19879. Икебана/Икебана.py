
g = lambda: [*map(int, input().split())]

n, m, h = g()
ans = 0
for _ in range(n):
    a, b = g()
    num = a + b * (m - 1)
    if num < h:
        ans = -1
        break
    if num > h:
        ans = 1
print(ans)