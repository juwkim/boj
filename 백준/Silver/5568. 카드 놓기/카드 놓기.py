from itertools import permutations
n = int(input())
k = int(input())

check = set()
nums = [input() for _ in range(n)]
for l in permutations(nums, k):
    check.add(''.join(l))
print(len(check))