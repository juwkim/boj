n = int(input())
ans, *nums = sorted(map(int, input().split()))
for num in nums:
    ans = (ans + num) / 2
print(ans)