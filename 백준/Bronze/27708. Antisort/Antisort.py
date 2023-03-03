T = int(input())
print(T)
for _ in range(T):
    input()
    print()
    N = int(input())
    print(N)
    nums = [*map(int, input().split())]
    if all(a < b for a, b in zip(nums, nums[1:])) or all(a > b for a, b in zip(nums, nums[1:])):
        nums[0], nums[1] = nums[1], nums[0]
    print(*nums)