n, m, *l = open(0).read().split()
n, m = int(n), int(m)
d = {}
cnt = 1
for i in range(n):
    for j in range(1, len(l[i]) + 1):
        d[cnt] = i + 1, j
        cnt += 1
for i in range(n, n + m):
    print(*d[int(l[i])])