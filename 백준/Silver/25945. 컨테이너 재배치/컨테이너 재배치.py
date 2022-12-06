n = int(input())
nums = sorted(map(int, input().split()))
q, r = divmod(sum(nums), n)
ans = 0
for i in range(n - r):
    ans += abs(nums[i] - q)

q += 1
for i in range(n - r, n):
    ans += abs(nums[i] - q)
print(ans // 2)