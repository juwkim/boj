g = lambda: [*map(int, input().split())]

for case in range(1, 1 + int(input())):
    N = int(input())
    nums = [g() for _ in range(N)]
    k = sum(nums[i][i] for i in range(N))
    r = sum(len(set(line)) != N for line in nums)
    c = sum(len(set(line)) != N for line in zip(*nums))
    print(f'Case #{case}: {k} {r} {c}')