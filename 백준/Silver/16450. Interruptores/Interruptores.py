g = lambda: [*map(int, input().split())]


N, M = g()
_, *nums = g()

nums = set(nums)
sw = [g()[1:] for _ in range(N)]

cnt = 0
while nums and cnt < N * 2:
    for num in sw[cnt % N]:
        if num in nums:
            nums.remove(num)
        else:
            nums.add(num)
    cnt += 1
if cnt == 2 * N:
    cnt = -1
print(cnt)