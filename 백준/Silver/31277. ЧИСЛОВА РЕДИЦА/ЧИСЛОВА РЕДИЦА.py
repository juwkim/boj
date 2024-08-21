N, *a = map(int, open(0).read().split())
cnt = {1: 0, 2: 0, 4: 0, 8: 0}
p, q = 0, 0
l, r = 0, 1
while r < N:
    if a[l] == a[r]:
        r += 1
    else:
        p = max(p, r - l)
        l, r = r, r + 1
p = max(p, r - l)
for i in range(N):
    cnt[a[i]] += 1
    if i - 4 >= 0:
        cnt[a[i - 4]] -= 1
    if all(val == 1 for val in cnt.values()):
        q += 1
print(p, q)