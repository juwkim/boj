l, d, n = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.append(-d + 6)
nums.append(l + d - 6)
nums.sort()
ans = 0
for i in range(n + 1):
    ans += (nums[i + 1] - nums[i] - d) // d
print(ans)