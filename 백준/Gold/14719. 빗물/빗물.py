H, W, *nums = map(int, open(0).read().split())
l, r = [0] * W, [0] * W
l[0], r[-1] = nums[0], nums[-1]
for i in range(1, W):
    l[i] = max(l[i - 1], nums[i])
    r[W - i - 1] = max(r[W - i], nums[W - i - 1])
ans = sum(max(0, min(l[i], r[i]) - nums[i]) for i in range(1, W - 1))
print(ans)