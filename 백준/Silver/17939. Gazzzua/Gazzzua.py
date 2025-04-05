N, *nums = map(int, open(0).read().split())
idx = sorted(range(N), key=lambda i: nums[i])
ans = 0
for i in range(N):
    if i == idx[-1]:
        idx.pop()
        continue
    while idx and idx[-1] < i:
        idx.pop()
    if not idx:
        break
    ans += nums[idx[-1]] - nums[i]
print(ans)