from itertools import combinations

*nums, h1, h2 = map(int, input().split())
ans = None
for l in combinations(nums, 3):
    if sum(l) == h1:
        ans = sorted(l, reverse=True)

for num in sorted(nums, reverse=True):
    if num not in ans:
        ans.append(num)
print(*ans)