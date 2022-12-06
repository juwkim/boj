g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
px = [0]
for i in range(N-1):
    px.append(px[-1] + nums[i])
ans = sum(a * b for a, b in zip(nums, px))
print(ans)