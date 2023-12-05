n = int(input())
nums = [[*map(int, input().split())] for _ in range(n)]
ans = min(range(n), key=lambda i: nums[i][1])
print(*nums[ans])