N = int(input())
nums = sorted(int(input()) for _ in range(N))
print(sum(nums) / N)
if N&1:
    print(nums[N//2])
else:
    print((nums[N//2-1] + nums[N//2]) / 2)