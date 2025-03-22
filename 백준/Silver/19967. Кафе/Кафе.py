n, m, k = map(int, input().split())
a = [['.'] * m for _ in range(n)]
for i in range(n % 3 != 1, n, 3):
    for j in range(m % 3 != 1, m, 3):
        a[i][j] = 'T'

for i in range(n):
    for j in range(m):
        if a[i][j] == '.':
            a[i][j] = 'h'
            k -= 1
            if k == 0:
                break
    if k == 0:
        break

if k:
    print("Impossible")
else:
    for l in a:
        print(*l, sep='')