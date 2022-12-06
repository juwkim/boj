def gcd(x, y):
	while y:
		x, y = y, x % y
	return x

def gcd_of_nums(lst):
	ret = lst[0]
	for num in lst[1:]:
		ret = gcd(ret, num)
	return ret

def solve(nums):
    if len(nums) <= 2:
        return sum(nums)
    mid = len(nums) // 2
    left = gcd_of_nums(nums[mid: ]) + solve(nums[ :mid])
    right = gcd_of_nums(nums[ :mid]) + solve(nums[mid: ])
    return max(left, right)
    
N = int(input())
nums = list(map(int, input().split()))
print(solve(nums))