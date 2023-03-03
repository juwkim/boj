nums = []
for _ in range(int(input())):
    num = int(input())
    if num >= 0:
        nums.append(num)
nums.sort()

ans = 0
for num in nums:
    if num != ans:
        break
    ans += 1
print(ans)