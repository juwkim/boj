def binary_search(num, left, right):
    
    if left > right:
        return left + (num > dp[left])
    
    mid = (left + right) // 2
    if dp[mid] == num:
        return mid
    elif dp[mid] > num:
        return binary_search(num, left, mid - 1)
    else:
        return binary_search(num, mid + 1, right)

N = int(input())
nums = [*map(int, input().split())]
dp = [0]
for num in nums:
    if num > dp[-1]:
        dp.append(num)
    elif num < dp[-1]:
        idx = binary_search(num, 1, len(dp) - 1)
        dp[idx] = min(dp[idx], num)
print(len(dp) - 1)