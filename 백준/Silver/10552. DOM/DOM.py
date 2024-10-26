import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M, P = g()
nums = [0] * (M + 1)
for _ in range(N):
    a, b = g()
    if not nums[b]:
        nums[b] = a
ans = 0
visited = bytearray(M + 1)
while nums[P]:
    if visited[nums[P]]:
        ans = -1
        break
    visited[nums[P]] = 1
    P = nums[P]
    ans += 1
print(ans)