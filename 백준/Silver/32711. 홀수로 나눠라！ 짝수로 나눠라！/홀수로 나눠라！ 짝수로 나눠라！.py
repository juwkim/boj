N, *nums = map(int, open(0).read().split())
cnt = sum(num & 1 for num in nums)
print(+(cnt & 1 or cnt > 2 or (cnt == 2 and (nums[0] % 2 == 0 or nums[-1] % 2 == 0)) or (cnt == 0 and N % 2 == 0)))