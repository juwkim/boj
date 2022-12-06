nums = [0]
for _ in range(int(input())):
    nums.append(int(input()) - nums[-1])

diff = (nums[-1] - nums[0]) // 2
for num in nums[:-1]:
    print(num + diff)
    diff *= -1