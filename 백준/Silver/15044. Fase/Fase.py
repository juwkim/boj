from collections import Counter
N = int(input())
K = int(input())
nums = Counter(int(input()) for _  in range(N))
ans = 0
for key in sorted(nums, reverse=True):
    if ans >= K:
        break
    ans += nums[key]
print(ans)