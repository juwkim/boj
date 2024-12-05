N, *nums = map(int, open(0).read().split())
ans, p, s = [], 0, sum(nums)
idx = sorted(range(N), key=lambda i: -nums[i])
for i in range(N - 2):
    s -= nums[i]
    while idx[-1] <= i: idx.pop()
    t = (s - nums[idx[-1]]) / (N - 2 - i)
    if t == p: ans.append(i + 1)
    elif t > p: ans, p = [i + 1], t
print(*ans)