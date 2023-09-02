N = int(input())
nums = sorted(map(int, input().split()))
print(sum(nums[:N//2]), sum(nums[N//2:]))