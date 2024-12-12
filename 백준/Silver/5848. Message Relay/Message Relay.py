N, *a = map(int, open(0))
loop = bytearray(N)
ans = 0
for i in range(N):
    visited = bytearray(N)
    nums, cur = [], i
    while True:
        if a[cur] == 0:
            ans += 1
            break
        if loop[cur] or visited[cur]:
            break
        nums.append(cur)
        visited[cur] = 1
        cur = a[cur] - 1
    if loop[cur]:
        for num in nums:
            loop[num] = 1
print(ans)