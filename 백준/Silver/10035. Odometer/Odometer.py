X, Y = map(int, input().split())
ans = 0
def solve(cur, num, other_used):
    if cur > Y:
        return
    global ans
    ans += other_used and X <= cur <= Y
    if cur < 10:
        for i in range(1, 10):
            if i != num:
                solve(i * 10 + cur, cur, True)
    if cur:
        solve(cur * 10 + num, num, other_used)
        if not other_used:
            for i in range(10):
                if i != num:
                    solve(cur * 10 + i, num, True)
for i in range(10):
    solve(i, i, False)
print(ans)