for _ in range(int(input())):
    input()
    nums = [*map(int, input().split())]
    max_num = max(nums)
    cnt = [0] * (1 << 20)
    for num in nums:
        cnt[num] += 1
    dp = cnt.copy()
    for i in range(20):
        for mask in range((1 << 20)):
            if mask & (1 << i):
                dp[mask] += dp[mask ^ (1 << i)]
    print(sum(dp[i] * cnt[i] for i in range(1 << 20)))