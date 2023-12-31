import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
nums = [int(input()) for _ in range(M)]
lo, hi = 0, max(nums)
while lo + 1 < hi:
    mid = (lo + hi) >> 1
    if sum((num + mid - 1) // mid for num in nums) <= N:
        hi = mid
    else:
        lo = mid
print(hi)