from itertools import combinations

N, *c = map(int, open(0).read().split())
nums = [1 / num for num in c]
ans = 0
for i in range(2, N + 1):
    for l in combinations(nums, i):
        if 0.99 <= sum(l) <= 1.01:
            ans += 1
print(ans)