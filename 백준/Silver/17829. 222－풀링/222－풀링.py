import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = [g() for _ in range(N)]
while len(nums) != 1:
    tmp = []
    for i in range(0, len(nums), 2):
        l = []
        for j in range(0, len(nums[i]), 2):
            p = sorted([nums[i][j], nums[i][j + 1], nums[i + 1][j], nums[i + 1][j + 1]])[2]
            l.append(p)
        tmp.append(l)
    nums = tmp
print(nums[0][0])