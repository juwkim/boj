n = int(input())
nums = sorted([int(input()) for _ in range(n)], reverse=True)
ans = n
for i in range(n):
    if nums[i] < i+1:
        ans = i
        break
print(ans)