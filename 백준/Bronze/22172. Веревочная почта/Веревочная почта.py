g = lambda: [*map(int, input().split())]

n = int(input())
nums = g()

s = max(0, max(nums[i] - i for i in range(n)) - 1)
t = max(0, max(i - nums[i] for i in range(n)) + 1)

print(s + t + min(s, t))