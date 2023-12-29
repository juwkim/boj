import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
nums = [int(input()) for _ in range(N)]
ans, cur = 0, 0
while cur != K:
    if nums[cur] == -1:
        ans = -1
        break
    nums[cur], cur = -1, nums[cur]
    ans += 1
print(ans)