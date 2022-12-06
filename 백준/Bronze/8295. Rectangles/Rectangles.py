nums = [*map(int, input().split())]
n, m = sorted(nums[:2])
p = -(nums[2]//-2)
total = 0
for i in range(p, n+m+1):
    for j in range(1, min(i, n+1)):
        total += max((n-j+1)*(m-i+j+1), 0)
print(total)