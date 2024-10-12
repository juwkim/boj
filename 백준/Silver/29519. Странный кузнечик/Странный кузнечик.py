N = int(input())
nums = [*map(int, input().split())]
if (N & N - 1) == 0 and (all(nums[2**i - 1 if 2**i - 1 < len(nums) else 0] == 1 for i in range(1, 16))):
    print("Yes")
else:
    print("No")