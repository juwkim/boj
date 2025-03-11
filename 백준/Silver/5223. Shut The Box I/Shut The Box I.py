import sys
input = sys.stdin.readline
from itertools import combinations

for _ in range(int(input())):
    t, n, *nums = map(int, input().split())
    nums.sort()
    ans = None
    for i in range(1, n + 1):
        for c in combinations(nums, i):
            if sum(c) == t and (ans == None or c > ans):
                ans = c
        if ans:
            break
    if ans:
        print(f"The best move is: {' '.join(map(str, ans))}")
    else:
        print("No move found.")