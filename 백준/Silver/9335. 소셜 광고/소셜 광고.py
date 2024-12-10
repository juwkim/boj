import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from itertools import combinations

for _ in range(int(input())):
    n = int(input())
    t = {*range(1, n + 1)}
    nums = []
    for i in range(1, n + 1):
        nums.append({*g()[1:]} | {i})
    for i in range(1, n + 1):
        for l in combinations(nums, i):
            s = set()
            for j in l:
                s |= j
            if s == t:
                print(i)
                break
        else:
            continue
        break