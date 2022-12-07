_, *nums = map(int, open(0))
keys = set(nums)
ans = 0
for key in keys:
    new = list(filter(lambda x: x != key, nums))
    prev, cnt = -1, 0
    for num in new:
        if num == prev:
            cnt += 1
        else:
            ans = max(ans, cnt)
            prev = num
            cnt = 1
    ans = max(ans, cnt)
print(ans)