C, N = map(int, input().split())
nums = [int(input()) for _ in range(N)]
ans = 0
def solve(num, idx):
    global ans
    if idx == N:
        ans = max(ans, num)
        return
    solve(num, idx + 1)
    if num + nums[idx] <= C:
        solve(num + nums[idx], idx + 1)
solve(0, 0)
print(ans)