N, *nums = map(int, open(0).read().split())
s = sum(nums)
ans, p = [], 0
idx = sorted(range(N), key=lambda i: nums[i], reverse=True)
for i in range(N - 2):
    s -= nums[i]
    while idx[-1] <= i:
        idx.pop()
    t = (s - nums[idx[-1]]) / (N - 2 - i)
    if t == p:
        ans.append(i + 1)
    elif t > p:
        ans, p = [i + 1], t
for num in ans:
    print(num)