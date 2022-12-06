from bisect import bisect_left
g = lambda: map(int, input().split())
N = int(input())
nums = sorted(g())
px = [0]
for i in range(N):
    px.append(px[-1] + nums[i])

Min = 1e9
ans = 0
for num in range(nums[0], nums[-1] + 1):
    idx = bisect_left(nums, num)
    l = idx * num - px[idx]
    r = px[-1] - px[idx] - (N - idx) * num
    diff = l + r
    if diff >= Min:
        break
    Min = diff
    ans = num
print(ans)