g = lambda: [*map(int, input().split())]

earn = 1
ans = 1e9
N = int(input())
nums = [g() for _ in range(N)]
for i in range(N):
    cost = nums[i][0]
    cur = 0
    for j in range(N):
        if nums[j][0] >= cost and nums[j][1] < cost:
            cur += cost - nums[j][1]
    if cur > earn:
        earn = cur
        ans = cost
    elif cur == earn:
        ans = min(ans, cost)
if ans == 1e9:
    ans = 0
print(ans)