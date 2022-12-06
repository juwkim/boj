import sys
input = lambda: sys.stdin.readline().rstrip('\n')
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N, M = g()
    nums = g()
    r, q = divmod(M, N)
    print(nums[-q-1] if r&1 else nums[q])