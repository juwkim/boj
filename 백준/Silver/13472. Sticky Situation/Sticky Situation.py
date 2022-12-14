g = lambda: [*map(int, input().split())]

N = int(input())
nums = sorted(g())
if any(nums[i] + nums[i+1] > nums[i+2] for i in range(N - 2)):
    ans = 'possible'
else:
    ans = 'impossible'
print(ans)