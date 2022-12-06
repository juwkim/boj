import sys

C = int(input())
for _ in range(C):
    nums = list(map(int, sys.stdin.readline().split()))
    N = nums[0]
    del nums[0]
    avg = sum(nums) / N
    
    total = N
    for num in nums:
        if num <= avg:
            total -= 1
    
    print("%.3f%%" % (total * 100 / N))