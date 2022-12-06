import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
for num in sorted(nums):
    print(num)