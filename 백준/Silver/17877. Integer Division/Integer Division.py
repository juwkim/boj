from collections import Counter

n, d, *a = map(int, open(0).read().split())
cnt = Counter([num // d for num in a])
ans = sum(cnt[i] * (cnt[i] - 1) // 2 for i in cnt)
print(ans)