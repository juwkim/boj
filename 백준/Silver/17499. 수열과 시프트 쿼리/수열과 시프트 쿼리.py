import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, Q = g()
a = g()
cur = 0
for _ in range(Q):
    op, *nums = g()
    if op == 1:
        i, x = nums
        a[(i - 1 - cur) % N] += x
    elif op == 2:
        cur += nums[0]
    else:
        cur -= nums[0]
cur %= N
if cur:
    print(*a[-cur:] + a[:-cur])
else:
    print(*a)