import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
nums = [[*map(int, input().split())] for _ in range(N)]
for l in permutations(range(N)):
    for i in range(N):
        p = sum(nums[l[i]])
        a = sum(sum(nums[l[j]]) < p for j in range(i))
        b = sum(sum(nums[l[j]]) < p for j in range(i + 1, N))
        if [a, b] != nums[l[i]]:
            break
    else:
        print("".join(chr(l[i] + 65) for i in range(N)))
        break