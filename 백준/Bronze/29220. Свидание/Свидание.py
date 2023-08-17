k = int(input())
n = int(input())
nums = [*map(int, input().split())]
if sum(nums) - min(nums) < k:
    print("NO")
else:
    print("YES")