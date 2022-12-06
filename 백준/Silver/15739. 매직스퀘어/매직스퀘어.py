g = lambda: [*map(int, input().split())]

N = int(input())
comp = N * (N * N + 1) // 2
nums = [g() for _ in range(N)]
if set(sum(nums, [])) == set(range(1, N*N+1)):
    nums += [*zip(*nums)]
    nums += [[nums[i][i] for i in range(N)]]
    nums += [[nums[N-1-i][i] for i in range(N)]]
    ans = all(sum(line) == comp for line in nums)
    print(['FALSE', 'TRUE'][ans])
else:
    print('FALSE')