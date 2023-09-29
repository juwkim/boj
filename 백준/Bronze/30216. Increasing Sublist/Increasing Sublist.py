import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
nums = g()
ans, cur = 0, 1
for i in range(1, n):
    if nums[i] > nums[i - 1]:
        cur += 1
    else:
        ans = max(ans, cur)
        cur = 1
ans = max(ans, cur)
print(ans)