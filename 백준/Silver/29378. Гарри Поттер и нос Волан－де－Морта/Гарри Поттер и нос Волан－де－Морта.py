n, m = map(int, input().split())
ans = 0
a = [input() for i in range(n)]
for i in range(n):
    for j in range(m - 1):
        ans += a[i][j] == '.' and a[i][j + 1] == '.'
for i in range(n - 1):
    for j in range(m):
        ans += a[i][j] == '.' and a[i + 1][j] == '.'
print(ans)