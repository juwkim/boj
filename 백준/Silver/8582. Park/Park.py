n = int(input())
nums = [int(input()) for _ in range(n)]
left = [nums[0]]
for i in range(1, n):
    left.append(max(left[-1], nums[i]))
right = [nums[-1]]
for i in range(n-2, -1, -1):
    right.append(max(right[-1], nums[i]))
right.reverse()
for i in range(n):
    print(left[i], right[i])