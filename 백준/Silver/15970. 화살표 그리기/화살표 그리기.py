g = lambda: [*map(int, input().split())]

N = int(input())
buf = [[-1e10, 1e10] for _ in range(N)]
for _ in range(N):
    pos, color = g()
    buf[color-1].append(pos)

ans = 0
for i in range(N):
    nums = sorted(buf[i]) 
    for j in range(1, len(nums) - 1):
        ans += min(nums[j] - nums[j-1], nums[j+1] - nums[j])
print(ans)