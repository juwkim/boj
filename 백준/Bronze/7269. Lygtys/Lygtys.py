import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
*nums, s = [int(input()) for _ in range(N)]
e = (sum(nums) - s) // (N - 2)
for num in nums:
    print(num - e)
print(e)