n, r = map(int, input().split())
nums = [*map(int, input().split())]
p = sum(nums)
area = 3.1415926535 * r * r
for num in nums:
    print(area * num / p)