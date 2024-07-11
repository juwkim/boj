N, *nums = map(int, open(0))
ans = 0
for i in range(N - 1, -1, -1):
    if nums[i] < i + 1 + ans:
        ans += 1
print(ans)