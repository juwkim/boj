input()
a = [*map(int, input().split())]
MAX = max(a)
cnt = [0] * (MAX + 1)
for num in a:
    cnt[num] += 1
ans = 0
for i in range(1, MAX + 1):
    if cnt[i] == 0:
        continue
    ans += cnt[i] * (cnt[i] - 1)
    for j in range(i * 2, MAX + 1, i):
        ans += cnt[i] * cnt[j]
print(ans)