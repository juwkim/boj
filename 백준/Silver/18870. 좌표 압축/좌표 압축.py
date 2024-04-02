from bisect import bisect_left

N, *nums = map(int, open(0).read().split())
s = sorted(set(nums))
print(*[bisect_left(s, num) for num in nums])