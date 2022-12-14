import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n, m = g()
nums = [int(input()) for _ in range(m)]
ans, check = [], set()
for i in range(m - 1, -1, -1):
    if nums[i] not in check:
        check.add(nums[i])
        ans.append(nums[i])
for i in range(1, n + 1):
    if i not in check:
        ans.append(i)
print(*ans)