import sys
input = sys.stdin.readline

nums = []
for _ in range(int(input())):
    r, k = map(int, input().split())
    nums.append((r / k, r))
ans, min_r = 0, 0
for rk, r in sorted(nums):
    if rk >= min_r:
        ans += 1
        min_r = r
    else:
        min_r = min(min_r, r)
print(ans)