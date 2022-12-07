g = lambda: [*map(int, input().split())]
N = int(input())
nums = g()
ans = 0
for i in range(N - 1, 0, -1):
    if nums[i - 1] > nums[i]:
        ans = i
        break
print(ans)