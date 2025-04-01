import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
nums = []
time = 0
for _ in range(N):
    t, K, *l = g()
    nums.extend(max(time, num) for num in l)
    time += t
    for i in range(len(nums)):
        nums[i] += t
print(sorted(nums)[min(len(nums), M) - 1])