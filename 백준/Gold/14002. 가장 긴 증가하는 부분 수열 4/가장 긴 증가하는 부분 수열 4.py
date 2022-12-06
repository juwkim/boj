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
p = []
for i, num in enumerate(nums):
    if num > dp[-1]:
        dp.append(num)
        p.append(len(dp) - 1)
    else:
        idx = binary_search(num, 1, len(dp) - 1)
        dp[idx] = num
        p.append(idx)

len_dp = len(dp) - 1
print(len_dp)

LIS, idx = [], -1
while len_dp:
    if p[idx] == len_dp:
        LIS.append(nums[idx])
        len_dp -= 1
    idx -= 1
print(*LIS[::-1])