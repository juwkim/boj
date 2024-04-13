N, S, *nums = map(int, open(0).read().split())
l, r, ans = 0, 0, 1e9
cur = nums[l]
while True:
    if cur >= S:
        ans = min(ans, r - l + 1)
        cur -= nums[l]
        l += 1
    elif r == N - 1: break
    else:
        r += 1
        cur += nums[r]
print(ans if ans != 1e9 else 0)