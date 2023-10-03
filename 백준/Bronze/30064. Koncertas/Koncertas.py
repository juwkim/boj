import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = [-1] + g()
ans, cur = 0, 1
while nums[cur]:
    ans += 1
    cur = nums[cur]
print(ans)