n = int(input())
a = [*map(int, input().split())]
pxa = [0] * (n - 1) + [a[-1]]
for i in range(n - 2, -1, -1):
    pxa[i] = a[i] + pxa[i + 1]
m = int(input())
b = [*map(int, input().split())]
pxb = [0] * (m - 1) + [b[-1]]
for i in range(m - 2, -1, -1):
    pxb[i] = b[i] + pxb[i + 1]
ans, cnt = min(pxa[0], pxb[0]), 0
i, j = 0, 0
while i < n and j < m:
    while i < n and a[i]:
        i += 1
    while j < m and b[j]:
        j += 1
    if i == n or j == m:
        break
    cnt += 1
    ans = max(ans, cnt + min(pxa[i], pxb[j]))
    i += 1
    j += 1
print(ans)