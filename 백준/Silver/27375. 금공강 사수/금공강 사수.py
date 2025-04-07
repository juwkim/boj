g = lambda: [*map(int, input().split())]

n, k = g()
nums = [g() for _ in range(n)]
ans = 0
def solve(i, check):
    global ans
    if i == n:
        ans += len(check) == k
        return
    solve(i + 1, check)
    w, s, e = nums[i]
    if w != 5:
        a = {*range((w - 1) * 10 + s - 1, (w - 1) * 10 + e)}
        if not check & a:
            p = check | a
            if len(p) <= k:
                solve(i + 1, p)
solve(0, set())
print(ans)