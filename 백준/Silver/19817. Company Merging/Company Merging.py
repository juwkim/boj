import sys
input = lambda: sys.stdin.readline()

g = lambda: [*map(int, input().split())]

nums = []
maxs = []
for _ in range(int(input())):
    n, *l = g()
    nums.append(n)
    maxs.append(max(l))

N = max(maxs)
ans = sum(a * (N - b) for a, b in zip(nums, maxs))
print(ans)