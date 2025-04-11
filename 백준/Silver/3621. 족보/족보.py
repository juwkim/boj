from collections import Counter

n, d, *nums = map(int, open(0).read().split())
print(sum(max(0, (v - 2) // (d - 1)) for v in Counter(nums).values()))