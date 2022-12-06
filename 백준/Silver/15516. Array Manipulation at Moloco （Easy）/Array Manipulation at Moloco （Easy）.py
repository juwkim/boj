nums = [int(input()) for _ in range(int(input()))]
for i in range(len(nums)):
    print(sum(nums[j] < nums[i] for j in range(i)))