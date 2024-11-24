import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = [*map(int, input().split())]
    ans = 0
    if n == 2:
        nums.sort()
        i = 1
        while nums[i] > 1:
            q = nums[i] >> 1
            ans += q
            nums[i] &= 1
            i ^= 1
            nums[i] += q
    elif any(num > 1 for num in nums):
        ans = sum(nums) - 1
        if nums.count(0) == n - 1:
            num = max(nums)
            if num <= 3:
                ans = 1
    print(ans)