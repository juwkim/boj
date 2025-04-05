N, *nums = map(int, open(0))
visited = bytearray(N)
ans = 0
for i in range(1, N):
    if visited[i]:
        continue
    ans += 1
    d = nums[i] - 1
    for j in range(i, N):
        if visited[j]:
            continue
        if nums[j] % d == 1:
            visited[j] = 1
print(ans)