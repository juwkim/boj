import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N = int(input())
nums = sorted((g(), i) for i in range(1, N + 1))
for i in range(N - 1):
    print(nums[i][1], nums[i + 1][1])