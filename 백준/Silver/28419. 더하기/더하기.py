import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
nums = g()
odd, even = sum(nums[::2]), sum(nums[1::2])
if n == 3 and odd > even:
    print(-1)
else:
    print(abs(odd - even))