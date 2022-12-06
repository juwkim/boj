import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    N = int(input())
    nums = g()
    Max, ans = 0, 0
    for i in range(N-1, -1, -1):
        Max = max(Max, nums[i])
        ans += max(0, Max - nums[i])
    print(ans)