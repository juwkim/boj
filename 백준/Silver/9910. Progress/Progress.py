k, *c = map(int, open(0).read().split())
idx = {num: i for i, num in enumerate(c)}
ans = 2
for i in range(k - 1):
    for j in range(i + 1, k):
        d = c[j] - c[i]
        num, last_idx = c[j] + d, j
        cur = 2
        while num in idx and idx[num] > last_idx:
            last_idx = idx[num]
            num += d
            cur += 1
        ans = max(ans, cur)
print(ans)