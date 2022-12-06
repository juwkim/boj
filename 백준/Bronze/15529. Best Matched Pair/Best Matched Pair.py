g = lambda: [*map(int, input().split())]

n = int(input())
nums = g()
ans = -1
for i in range(n-1):
    for j in range(i+1, n):
        mul = nums[i] * nums[j]
        if str(mul) in '123456789':
            ans = max(ans, mul)
print(ans)