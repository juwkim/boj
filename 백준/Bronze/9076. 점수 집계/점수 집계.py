import sys
for _ in range(int(sys.stdin.readline())):
    nums = sorted(map(int, sys.stdin.readline().split()))
    print(sum(nums[1:4]) if nums[3] - nums[1] < 4 else "KIN")