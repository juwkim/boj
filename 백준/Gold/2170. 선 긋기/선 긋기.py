import sys
input = sys.stdin.readline

ans = 0
N = int(input())
nums = [[*map(int, input().split())] for _ in range(N)]
nums.sort()
p, q = nums[0]
for i in range(1, N):
    x, y = nums[i]
    if x <= q:
        q = max(q, y)
    else:
        ans += q - p
        p, q = x, y
ans += q - p
print(ans)