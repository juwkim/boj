N, *nums, K = map(int, open(0).read().split())
cnt = [0] * (2 + nums[-1] * K)
for num in nums: cnt[num] = 1
i = 1
while cnt[i]:
    if cnt[i] < K:
        for num in nums:
            if cnt[i + num]: continue
            cnt[i + num] = cnt[i] + 1
    i += 1
print(f"{('hol', 'jjak')[i & 1]}soon win at {i}")