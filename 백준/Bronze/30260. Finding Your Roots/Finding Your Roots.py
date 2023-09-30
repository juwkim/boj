import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    L, n = g()
    nums = [0] + g()
    ans = 1
    while nums[L]:
        L = nums[L]
        ans += 1
    print(f'Data Set {tc}:')
    print(ans)
    print()