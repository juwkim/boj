import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, K = g()
nums = [g() + [i] for i in range(1, N + 1)]
for i in range(K):
    nums.sort(key=lambda x: x[i])
if nums == sorted(nums):
    print("YES")
    print(*[x[-1] for x in nums])
else:
    print("NO")