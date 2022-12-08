from math import lcm
N = int(input())
ans, *nums = map(int, input().split())
for num in nums:
    ans = lcm(ans, num)
print(ans)