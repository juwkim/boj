import sys
input = lambda: sys.stdin.readline().rstrip('\n')
g = lambda: [*map(int, input().split())]

ans = 0
now = 0
n = int(input())
for _ in range(n):
    nums = g()
    nums += [0, 0] + nums
    idx = nums.index(1, now)
    ans += idx - now + 1
    now = (idx + 1) % 7
print(ans)