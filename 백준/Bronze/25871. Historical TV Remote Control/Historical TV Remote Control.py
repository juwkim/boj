nums = set(input().split()[1:])
ans = 1000
t = int(input())
for num in range(1000):
    if all(i not in nums for i in str(num)):
        ans = min(ans, abs(num - t))
print(ans)