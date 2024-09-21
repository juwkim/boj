import sys
input = sys.stdin.readline

N = int(input())
if N & 1:
    print(1)
else:
    nums = []
    for _ in range(N):
        A, B = map(int, input().split())
        nums.append(A - B)
    nums.sort()
    print(nums[N//2] - nums[N//2 - 1] + 1)