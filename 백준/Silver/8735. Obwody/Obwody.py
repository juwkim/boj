import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]


n = int(input())
nums = [g() for _ in range(n)]
nums.sort(key=lambda x: x[1] - x[0])

cur = 0
ans = n
for i in range(n):
    d, b = nums[i]
    cur += d - b
    if cur < 0:
        ans = i
        break
print(ans)