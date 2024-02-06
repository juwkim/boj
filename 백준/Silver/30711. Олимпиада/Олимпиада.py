import sys
input = lambda: sys.stdin.readline().rstrip()

from bisect import bisect

n, p, c = map(int, input().split())
ans = [""] * n
a = [(i, int(input())) for i in range(n)]
nums = sorted(num[1] for num in a)
for i, num in a:
    idx1 = bisect(nums, num - c)
    rank1 = n + 1 - idx1
    if rank1 <= p + 1:
        ans[i] = "Pass"
        continue
    idx2 = bisect(nums, num + c)
    rank2 = n + 1 - idx2
    if rank2 <= p:
        ans[i] = "Short"
    else:
        ans[i] = "Fail"
print(*ans)