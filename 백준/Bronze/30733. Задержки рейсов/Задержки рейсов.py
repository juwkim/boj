n, k, *t = map(int, open(0).read().split())
cur = t[0] - k
for i in range(n):
    cur = max(t[i], cur + k)
    print(cur, end=' ')