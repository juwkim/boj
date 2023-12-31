import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
W = tuple(map(int, input().split()))
dic = {}
def solve(nums):
    if nums in dic:
        return dic[nums]
    if len(nums) == 3:
        return nums[0] * nums[2]
    ret = 0
    for i in range(1, len(nums) - 1):
        ret = max(ret, nums[i-1] * nums[i+1] + solve(nums[:i] + nums[i+1:]))
    dic[nums] = ret
    return ret
ans = solve(W)
print(ans)