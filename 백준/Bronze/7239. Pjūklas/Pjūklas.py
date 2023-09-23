import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = sorted(g())
ans = [nums[0]]
cur = -1
d = [3, -1]
for i in range(N - 1):
    cur += d[i&1]
    if cur >= N:
        cur -= 1
    ans.append(nums[cur])
print(*ans)