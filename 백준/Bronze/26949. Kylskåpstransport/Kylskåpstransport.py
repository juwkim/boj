pa, ka, pb, kb, n = map(int, input().split())

x, y, ans = None, None, 1e9
for i in range((n + ka - 1) // ka + 1):
    j = (n - ka * i + kb - 1) // kb
    cost = i * pa + j * pb
    if cost < ans:
        ans = cost
        x, y = i, j
print(x, y, ans)