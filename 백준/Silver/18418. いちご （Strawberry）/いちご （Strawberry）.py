import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = sorted([g() for _ in range(N)], reverse=True)
time = max(nums[0])
for (A1, T1), (A2, T2) in zip(nums, nums[1:]):
    time = max(time + A1 - A2, T2)
time += nums[-1][0]
print(time)