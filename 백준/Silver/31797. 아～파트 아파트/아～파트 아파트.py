import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
nums = []
for i in range(1, M + 1):
    h1, h2 = g()
    nums.append((h1, i))
    nums.append((h2, i))
nums.sort()
ans = nums[(N - 1) % (2 * M)][1]
print(ans)