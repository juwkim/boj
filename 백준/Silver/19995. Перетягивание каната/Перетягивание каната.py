n, d, *a = map(int, open(0).read().split())
ans, *nums = sorted(a, reverse=True)
check = ans < 3 * d
for num in nums:
    if num <= 2 * d:
        break
    ans += num - 2 * d
    if num < 3 * d:
        if check:
            break
        check = True
print(ans)