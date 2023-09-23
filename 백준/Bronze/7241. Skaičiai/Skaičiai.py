import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import permutations

nums = []
for a, b, c in permutations(g(), 3):
    nums.append(a * 100 + b * 10 + c)
nums.sort()
ans = nums.index(int(input())) + 1
print(ans)