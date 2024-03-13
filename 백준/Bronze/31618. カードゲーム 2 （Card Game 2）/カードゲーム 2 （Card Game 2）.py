N, *nums = map(int, open(0).read().split())
nums = set(nums)
ans = "No"
for num in range(min(nums), max(nums) - 5):
    if all(i in nums for i in (num, num + 3, num + 6)):
        ans = "Yes"
        break
print(ans)