input()
cur, *nums = map(int, input().split())
ans = 'Yes'
for num in sorted(nums):
    if num < cur:
        cur += num
    else:
        ans = 'No'
        break
print(ans)