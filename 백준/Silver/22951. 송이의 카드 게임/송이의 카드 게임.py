g = lambda: [*map(int, input().split())]

N, K = g()
nums = [g() for i in range(N)]
cnt = [K] * N
i, j = 0, 0
for _ in range(N*K-1):
    num = nums[i].pop(j)
    cnt[i] -= 1
    j += num - 1
    while j >= cnt[i]:
        j -= cnt[i]
        i = (i + 1) % N
    
idx = cnt.index(1)
print(idx + 1, nums[idx][0])