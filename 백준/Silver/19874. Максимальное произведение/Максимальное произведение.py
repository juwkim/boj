g = lambda: [*map(int, input().split())]

n = int(input())
nums = g()
for i in range(1, n):
    nums[i] += nums[i-1]

ans = 0
Max = 0
for i in range(n-1):
    num = nums[i] * (nums[-1] - nums[i])
    if num > Max:
        Max = num
        ans = i
print(ans + 1)