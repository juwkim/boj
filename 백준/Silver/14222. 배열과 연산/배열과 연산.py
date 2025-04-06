N, K, *A = map(int, open(0).read().split())
visited = bytearray(N + 1)
ans = 1
for num in sorted(A):
    cur = num
    while cur <= N and visited[cur]:
        cur += K
    if cur > N:
        ans = 0
        break
    visited[cur] = 1
print(ans)