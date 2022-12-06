g = lambda: [*map(int, input().split())]

N, K = g()
nums = []
for i in range(1, N+1):
    tmp = g() + [i]
    nums.append(tmp)
nums.sort()
nums = nums[-K:]
ans = max(nums, key=lambda x: x[1])[2]
print(ans)