n, m = map(int, input().split())
paint = sorted(int(input()) for _ in range(n))
nums = sorted(int(input()) for _ in range(m))
ans, i, j = 0, 0, 0
while j < m:
    if paint[i] < nums[j]:
        i += 1
    else:
        ans += paint[i] - nums[j]
        j += 1
print(ans)