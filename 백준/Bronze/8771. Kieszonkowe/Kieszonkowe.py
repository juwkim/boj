import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    n = int(input())
    nums = g()
    a = sum(nums)
    b = 1
    i = 0
    while a > b and i < n:
        b *= nums[i]
        i += 1
    
    print(['=', 'SUMA', 'ILOCZYN'][(a > b) - (a < b)])