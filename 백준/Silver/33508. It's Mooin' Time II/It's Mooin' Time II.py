from collections import Counter

N, *a = map(int, open(0).read().split())
cnt = Counter(a)
twos = sum(v >= 2 for v in cnt.values())
visited = set()
ans = 0
for i in range(N - 2):
    x = a[i]
    cnt[x] -= 1
    if cnt[x] == 1:
        twos -= 1
    if x not in visited:
        visited.add(x)
        ans += twos - (cnt[x] >= 2)
print(ans)