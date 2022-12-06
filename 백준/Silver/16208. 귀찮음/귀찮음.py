g = lambda: [*map(int, input().split())]

n = int(input())
nums = sorted(g())
Sum = sum(nums)
ans = 0
for i in range(n-1):
    tmp = nums.pop()
    Sum -= tmp
    ans += Sum * tmp
print(ans)