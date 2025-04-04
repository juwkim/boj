g = lambda: map(int, input().split())

n, m, k = g()
quest = [{*g()} for _ in range(m)]
ans = 1
def solve(i, cur, cnt):
    global ans
    if i == m:
        ans = max(ans, cnt)
        return
    solve(i + 1, cur, cnt)
    new = cur | quest[i]
    if len(new) <= n:
        solve(i + 1, new, cnt + 1)
solve(0, set(), 0)
print(ans)