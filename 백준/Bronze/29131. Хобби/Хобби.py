import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
nums = sorted([g(), i] for i in range(1, n + 1))
print(n // 2)
for i in range(1, n, 2):
    print(nums[i - 1][1], nums[i][1])