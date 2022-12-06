from math import dist, pi
g = lambda: [*map(int, input().split())]
n, r = g()
nums = [g() for _ in range(n)]
nums.append(nums[0])

ans = n * 4 * pi * r**3 / 3
for i in range(n):
    d = dist(nums[i], nums[i+1])
    ans -= 2 * pi * (2*r + d/2) * (r - d/2)**2 / 3

print(ans)