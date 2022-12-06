from math import gcd, isqrt
N = int(input())
nums = sorted(int(input()) for _ in range(N))
GCD = nums[1] - nums[0]
for i in range(1, N-1):
    GCD = gcd(GCD, nums[i+1] - nums[i])

buf = {GCD}
for i in range(2, 1 + isqrt(GCD)):
    r, q = divmod(GCD, i)
    if q == 0:
        buf.add(r)
        buf.add(i)
print(*sorted(buf))