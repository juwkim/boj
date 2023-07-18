N = int(input())
ans = 1
s, *nums = map(int, input().split())
for num in nums:
    if s + num & 1:
        s = num
        ans += 1
print(ans)