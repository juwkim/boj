N = int(input())
nums = [int(input()) for _ in range(N)]
print(max(0, min(nums) - max(nums) // 2))