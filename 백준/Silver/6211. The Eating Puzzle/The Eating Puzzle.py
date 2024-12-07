def solve(i, cnt):
    global ans
    if cnt <= C:
        ans = max(ans, cnt)
    if i == B or cnt >= C:
        return
    solve(i + 1, cnt)
    solve(i + 1, cnt + L[i])

C, B, *L = map(int, open(0).read().split())
ans = 0
solve(0, 0)
print(ans)