import sys
input = sys.stdin.readline
from itertools import combinations

for _ in range(int(input())):
    x = int(input())
    nums = [*map(int, input().split())]
    w = int(input())
    ans = "Not possible"
    for i in range(1, x + 1):
        if any(sum(l) == w for l in combinations(nums, i)):
            ans = i
            break
    print(ans)