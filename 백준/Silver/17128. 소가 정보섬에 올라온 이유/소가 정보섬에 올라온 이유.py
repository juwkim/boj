import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, Q = g()
A = g()
nums = [A[i] * A[(i + 1) % N] * A[(i + 2) % N] * A[(i + 3) % N] for i in range(N)]
ans = sum(nums)
for Q in g():
    for i in range(Q - 1, Q - 5, -1):
        nums[i] *= -1
        ans += 2 * nums[i]
    print(ans)