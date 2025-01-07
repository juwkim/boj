N = int(input())
nums = [0] + [int(input()) for _ in range(N)]
visited = bytearray(N + 1)
ans = 0
for i in range(1, N + 1):
    if visited[i]: continue
    ans += 1
    visited[i] = 1
    cur = i
    while nums[cur] != i:
        cur = nums[cur]
        visited[cur] = 1
print(ans)