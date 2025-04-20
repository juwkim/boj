import sys
g = lambda: map(int, sys.stdin.readline().split())

N, X, Y, Z = g()
nums = []
for _ in range(N):
    A, B = g()
    nums.extend(((A, Y - X), (B + 1, Z - Y)))
nums.sort(reverse=True)
ans = cur = N * X
while nums:
    T = nums[-1][0]
    while nums and nums[-1][0] == T:
        cur += nums.pop()[1]
    ans = max(ans, cur)
print(ans)