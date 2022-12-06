import sys
input = lambda: sys.stdin.readline().rstrip()


g = lambda: [*map(int, input().split())]



n, k = g()
nums = g()
ans = 1
cur = 1
for i in range(n-1):
    if nums[i] == nums[i+1]:
        ans = max(ans, cur)
        cur = 1
    else:
        cur += 1
ans = max(ans, cur)
print(ans)