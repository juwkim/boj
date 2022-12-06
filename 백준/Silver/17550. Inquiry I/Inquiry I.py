import sys
input = lambda: sys.stdin.readline().rstrip('\n')

nums = [0]
nums_2 = [0]
N = int(input())
for _ in range(N):
    num = int(input())
    nums.append(nums[-1] + num)
    nums_2.append(nums_2[-1] + num ** 2)

ans = 0
for i in range(1, N):
    ans = max(ans, nums_2[i] * (nums[-1] - nums[i]))
print(ans)