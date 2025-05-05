from functools import lru_cache

for line in open(0):
    n, *nums = map(int, line.split())
    nums = tuple(nums)
    ans = 1e9
    @lru_cache(None)
    def solve(left, cnt, l):
        global ans
        if not l:
            ans = min(ans, cnt)
            return
        for i in range(len(l)):
            if l[i] > left:
                solve(n - l[i], cnt + 1, l[:i] + l[i + 1:])
            else:
                solve(left - l[i], cnt, l[:i] + l[i + 1:])
    solve(n, 1, nums)
    print(ans)