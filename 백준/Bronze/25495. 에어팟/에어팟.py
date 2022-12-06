g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
ans, cur = 2, 2
for i in range(1, N):
    if nums[i-1] == nums[i]:
        cur <<= 1
    else:
        cur = 2
    ans += cur
    if ans >= 100:
        ans = 0
        cur = 1
print(ans)