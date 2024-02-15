_, *a = map(int, open(0).read().split())
MAX = max(a)
cnt = [0] * (MAX + 1)
for num in a:
    cnt[num] += 1
ans = 0
for i in range(1, MAX + 1):
    SUM = -1
    for j in range(i, MAX + 1, i):
        SUM += cnt[j]
    ans += cnt[i] * SUM
print(ans)