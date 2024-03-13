n, k, *nums = map(int, open(0).read().split())
win = sum(i * num for i, num in zip(range(1, k + 1), nums))
cur = sum(nums[:k])
buf = []
for i in range(1, n - k + 1):
    buf.append((win, i))
    win += nums[i + k - 1] * k - cur
    cur += nums[i + k - 1] - nums[i - 1]
buf.append((win, n - k + 1))
for win, i in sorted(buf):
    print(i, win)