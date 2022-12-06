import sys

def binary_search(num, nums, left, right):
    while(right >= left):
        middle = (left + right) // 2
        if num == nums[middle]:
            return True
        elif num > nums[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return False

sys.stdin.readline()
ans = sorted(set(sys.stdin.readline().split()))
sys.stdin.readline()
nums = sys.stdin.readline().split()
N = len(ans) - 1

for num in nums:
    print(1 if binary_search(num, ans, 0, N) else 0)