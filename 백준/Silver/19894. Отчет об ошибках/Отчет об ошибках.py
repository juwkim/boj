n, m, *f = map(int, open(0).read().split())
if len({*f}) <= 2:
    print(0)
else:
    nums = [set() for _ in range(n + 1)]
    for i in range(m - 1):
        nums[f[i + 1]].add(f[i])
    idx = max({*range(n + 1)} - {f[-1]}, key=lambda i: len(nums[i]))
    ans = []
    for i in range(1, n + 1):
        if i in (idx, f[0]):
            continue
        for j in nums[i]:
            ans.append((i, j))
    print(len(ans))
    for a, b in ans:
        print(a, b)