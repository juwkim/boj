N, *nums = map(int, open(0))
nums = [0] + nums
selected = bytearray(N + 1)
for i in range(1, N + 1):
    if selected[i]:
        continue
    visited = bytearray(N + 1)
    visited[i] = 1
    cur, success = i, False
    while True:
        num = nums[cur]
        if num == i:
            success = True
            break
        if selected[num] or visited[num]:
            break
        visited[num] = 1
        cur = num
    if success:
        for j in range(1, N + 1):
            selected[j] |= visited[j]
print(sum(selected))
for i in range(1, N + 1):
    if selected[i]:
        print(i)