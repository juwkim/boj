g = lambda: [*map(int, input().split())]

A = g()
cnt = [0] * 7
for num in g():
    cnt[num] += 1

for i in range(2, 7):
    cnt[i] += cnt[i - 1]

ans, total = 0, 36
for num in A:
    ans += cnt[num - 1]
    total -= cnt[num] - cnt[num - 1]
ans /= total
print("%.5f" % ans)