def binary_search_up(dp, num, left, right):
    
    if left > right:
        return left + (num > dp[left])
    
    mid = (left + right) // 2
    if dp[mid] == num:
        return mid
    elif dp[mid] > num:
        return binary_search_up(dp, num, left, mid - 1)
    else:
        return binary_search_up(dp, num, mid + 1, right)

def binary_search_down(dp, num, left, right):
    
    if left > right:
        return right + (num < dp[right])
    
    mid = (left + right) // 2
    if dp[mid] == num:
        return mid
    elif dp[mid] < num:
        return binary_search_down(dp, num, left, mid - 1)
    else:
        return binary_search_down(dp, num, mid + 1, right)

def get_LIS(i):
    dp = [0]
    array = [k for k in nums[:i] if k < nums[i]]
    for num in array:
        if num > dp[-1]:
            dp.append(num)
        elif num < dp[-1]:
            idx = binary_search_up(dp, num, 1, len(dp) - 1)
            dp[idx] = num
    return len(dp) - 1


def get_LDS(i):
    dp = [1001]
    array = [k for k in nums[i+1:] if k < nums[i]]
    for num in array:
        if num < dp[-1]:
            dp.append(num)
        elif num > dp[-1]:
            idx = binary_search_down(dp, num, 1, len(dp) - 1)
            dp[idx] = num
    return len(dp) - 1

def solve(i):
    return get_LIS(i) + get_LDS(i) + 1

N = int(input())
nums = [*map(int, input().split())]
print(max(solve(i) for i in range(len(nums))))