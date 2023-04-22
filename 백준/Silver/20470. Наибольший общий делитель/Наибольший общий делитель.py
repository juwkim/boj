from math import gcd

n, d = map(int, input().split())
nums = [*map(int, input().split())]

ans = None
for i in range(n - 1):
    for j in range(1, n):
        if gcd(nums[i], nums[j]) == d:
            ans = nums[i], nums[j]
            break
    else:
        continue
    break

if ans:
    print(2)
    print(*ans)
else:
    print(-1)   