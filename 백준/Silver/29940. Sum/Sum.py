import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, S = g()
nums = [int(input()) for _ in range(N)]
ans = 0
l, r = 0, N - 1
while l < r:
    cur = nums[l] + nums[r]
    if cur == S:
        ans += 1
        l, r = l + 1, r - 1
    elif cur > S:
        r -= 1
    else:
        l += 1
print(ans)