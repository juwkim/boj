from collections import Counter

N, *nums = map(int, open(0).read().split())
cnt = Counter()
for num in nums:
    mask = 0
    while True:
        num, r = divmod(num, 10)
        mask |= 1 << r
        if num == 0:
            break
    cnt[mask] += 1
masks = [*cnt]
ans = 0
for i in range(len(masks)):
    ans += cnt[masks[i]] * (cnt[masks[i]] - 1) >> 1
    for j in range(i + 1, len(masks)):
        if masks[i] & masks[j]:
            ans += cnt[masks[i]] * cnt[masks[j]]
print(ans)