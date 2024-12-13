import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
nums = [0] * 100
for _ in range(N):
    s, t, c = g()
    for i in range(s - 1, t):
        nums[i] += c
aircons = [g() for _ in range(M)]
ans = 1e9
def solve(i, cost):
    global ans
    if i == M:
        return
    solve(i + 1, cost)
    a, b, p, m = aircons[i]
    for j in range(a - 1, b):
        nums[j] -= p
    if all(x <= 0 for x in nums):
        ans = min(ans, cost + m)
    else:
        solve(i + 1, cost + m)
    for j in range(a - 1, b):
        nums[j] += p
solve(0, 0)
print(ans)