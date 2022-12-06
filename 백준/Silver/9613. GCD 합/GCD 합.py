g = lambda: [*map(int, input().split())]

from math import gcd
for _ in range(int(input())):
    n, *nums = g()
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += gcd(nums[i], nums[j])
    print(ans)