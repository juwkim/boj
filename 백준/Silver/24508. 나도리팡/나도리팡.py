ans = 0
N, K, T = map(int, input().split())
nums = sorted(map(int, input().split()))
left, right = 0, N - 1

while left < right and ans <= T:
    if nums[left] + nums[right] > K:
        nums[left] -= K - nums[right]
        ans += K - nums[right]
        right -= 1
    elif nums[left] + nums[right] < K:
        nums[right] += nums[left]
        ans += nums[left]
        left += 1
    else:
        ans += nums[left]
        left += 1
        right -= 1

if ans > T:
    print("NO")
elif left > right:
    print("YES")
elif nums[left] == 0:
    print("YES")
else:
    print("NO")