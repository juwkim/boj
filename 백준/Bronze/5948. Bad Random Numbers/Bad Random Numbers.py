n = int(input())
nums = []
while n not in nums:
    nums.append(n)
    n = (n%1000//10)**2
print(len(nums))