n, L, *nums = map(int, open(0).read().split())
ans, last = 0, -1e9
for d in sorted(nums):
    if d - last < L:
        ans += 1
    else:
        last = d
print(ans)