input()
nums = sorted(map(int, input().split()))
ans = sum(nums)
if ans & 1:
    for num in nums:
        if num & 1:
            ans -= num
            break
if ans:
    print(ans)
else:
    print('NIESTETY')