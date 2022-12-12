N = int(input())
nums = [0] + [*map(int, input().split())]
for i in range(1, N + 1):
    nums[i] += nums[i-1]
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(nums[b+1] - nums[a])