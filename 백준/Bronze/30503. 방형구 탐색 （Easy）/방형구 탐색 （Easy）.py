import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
for _ in range(int(input())):
    s = g()
    if len(s) == 4:
        _, l, r, k = s
        cnt = nums[l-1:r].count(k)
        print(cnt)
    else:
        _, l, r = s
        nums[l-1:r] = [0] * (r - l + 1)