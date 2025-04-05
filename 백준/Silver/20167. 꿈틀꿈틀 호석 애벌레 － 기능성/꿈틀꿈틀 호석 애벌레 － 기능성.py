N, K, *nums = map(int, open(0).read().split())

ans = 0
def solve(i, cur, good):
    global ans
    if cur >= K:
        good += cur - K
        cur = 0
    if i == N:
        ans = max(ans, good)
        return
    solve(i + 1, cur + nums[i], good)
    if cur == 0:
        solve(i + 1, cur, good)
solve(0, 0, 0)
print(ans)