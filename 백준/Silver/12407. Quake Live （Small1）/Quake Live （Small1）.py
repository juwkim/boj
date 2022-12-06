g = lambda: [*map(int, input().split())]

from itertools import combinations
for _ in range(1, 1 + int(input())):
    N, *nums = g()
    Sum = sum(nums)
    num = min(abs(2 * sum(l) - Sum) for l in combinations(nums, N//2))
    print(f'Case #{_}: {num}')