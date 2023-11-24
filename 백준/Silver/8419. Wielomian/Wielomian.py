import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

s, x = g()
ans, *nums = g()
for num in nums:
    ans = ans * x + num
print("%03d" % (abs(ans) % 1000))