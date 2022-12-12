from copy import deepcopy
n = int(input())
nums = [0] * n
ans = []
check = set()
def solve(step):
    if nums != sorted(nums, reverse=True):
        return
    s = tuple(nums)
    if s in check:
        return
    check.add(s)
    if step == 0:
        ans.append(deepcopy(nums))
        return
    
    for i in range(n):
        nums[i] += 1
        solve(step - 1)
        nums[i] -= 1

solve(n)
for line in sorted(ans, reverse=True):
    for num in line:
        if num:
            print(num, end=' ')
    print()