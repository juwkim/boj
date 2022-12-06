while True:
    nums = input()
    if nums == '0':
        break
    zeros, ones = nums.count('0'), nums.count('1')
    print(4 * len(nums) + zeros - ones + 1)