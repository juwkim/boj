import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N = int(input())
nums = [0]
for m in g():
    nums.append(nums[-1] + m)
ans = 0
for _ in range(int(input())):
    a, t = g()
    if nums[a] > t:
        ans = -1
        break
    ans = max(ans, 2 * nums[a])
print(ans)