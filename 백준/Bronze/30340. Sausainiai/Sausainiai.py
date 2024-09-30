import sys
input = sys.stdin.readline

N = int(input())
nums = sorted([[*map(int, input().split())] for _ in range(N)], key=lambda x: (-abs(x[0] - x[1]), -x[0]))
ans = 0
for i in range(N):
    if i & 1:
        ans -= nums[i][1]
    else:
        ans += nums[i][0]
print(ans)